from inspect import isasyncgen, isgenerator
from typing import Any, Callable

from ididi import Graph
from ididi.graph import Resolver
from starlette.requests import Request
from starlette.responses import Response, StreamingResponse

from lihil.config import EndPointConfig
from lihil.endpoint import EndpointSignature, ParseResult
from lihil.endpoint.returns import agen_encode_wrapper, syncgen_encode_wrapper
from lihil.errors import InvalidParamTypeError
from lihil.interface import HTTP_METHODS, IReceive, IScope, ISend
from lihil.plugins.bus import BusTerminal, EventBus
from lihil.problems import InvalidRequestErrors, get_solver
from lihil.utils.threading import async_wrapper


class Endpoint[R]:
    def __init__(
        self,
        path: str,
        method: HTTP_METHODS,
        tag: str,
        func: Callable[..., R],
        graph: Graph,
        busterm: BusTerminal,
        config: EndPointConfig,
    ):
        self._path = path
        self._method: HTTP_METHODS = method
        self._tag = tag
        self._unwrapped_func = func
        self._func = async_wrapper(func, threaded=config.to_thread)
        self._graph = graph
        self._busterm = busterm
        self._config = config
        self._name = func.__name__

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._method}: {self._path!r} {self._func})"

    @property
    def config(self):
        return self._config

    @property
    def path(self) -> str:
        return self._path

    @property
    def name(self) -> str:
        return self._name

    @property
    def sig(self) -> EndpointSignature[R]:
        return self._sig

    @property
    def method(self) -> HTTP_METHODS:
        return self._method

    @property
    def scoped(self) -> bool:
        return self._scoped

    @property
    def encoder(self):
        return self._encoder

    @property
    def tag(self) -> str:
        return self._tag

    @property
    def unwrapped_func(self) -> Callable[..., R]:
        return self._unwrapped_func

    def setup(self) -> None:
        self._sig = EndpointSignature.from_function(
            graph=self._graph,
            route_path=self._path,
            f=self._unwrapped_func,
        )

        self._dep_items = self._sig.dependencies.items()
        self._plugin_items = self._sig.plugins.items()

        self._static = not any(
            (
                self._sig.path_params,
                self.sig.query_params,
                self.sig.header_params,
                self.sig.body_param,
                self.sig.dependencies,
                self.sig.plugins,
            )
        )

        scoped_by_config = bool(self._config and self._config.scoped is True)

        self._require_body: bool = self._sig.body_param is not None
        self._status_code = self._sig.default_status
        self._scoped: bool = self._sig.scoped or scoped_by_config
        self._encoder = self._sig.return_encoder

    def sync_deps(self, graph: Graph, busterm: BusTerminal):
        self._graph = graph
        self._busterm = busterm

    async def inject_plugins(
        self, params: dict[str, Any], request: Request, resolver: Resolver
    ):
        for name, p in self._plugin_items:
            ptype = p.type_
            if issubclass(ptype, Request):
                params[name] = request
            elif issubclass(ptype, EventBus):
                bus = self._busterm.create_event_bus(resolver)
                params[name] = bus
            elif issubclass(ptype, Resolver):
                params[name] = resolver
            elif p.loader:  # TODO? read form here
                params[name] = await p.loader(request, resolver)
            else:
                raise InvalidParamTypeError(ptype)
        return params

    async def make_static_call(self, scope: IScope, receive: IReceive, send: ISend):
        try:
            return await self._func()
        except Exception as exc:
            request = Request(scope, receive, send)
            if solver := get_solver(exc):
                return solver(request, exc)
            raise

    async def make_call(
        self, scope: IScope, receive: IReceive, send: ISend, resolver: Resolver
    ) -> R | ParseResult | Response:
        request = Request(scope, receive, send)
        callbacks = None

        try:
            if self._require_body:
                parsed_result = await self._sig.parse_command(request)
            else:
                parsed_result = self._sig.parse_query(request)
            callbacks = parsed_result.callbacks
            if errors := parsed_result.errors:
                raise InvalidRequestErrors(detail=errors)

            if self._plugin_items:
                params = await self.inject_plugins(
                    parsed_result.params, request, resolver
                )
            else:
                params = parsed_result.params

            for name, dep in self._dep_items:
                params[name] = await resolver.aresolve(dep.dependent, **params)

            raw_return = await self._func(**params)
            return raw_return
        except Exception as exc:
            if solver := get_solver(exc):
                return solver(request, exc)
            raise
        finally:
            if callbacks:
                for cb in callbacks:
                    await cb()

    def return_to_response(self, raw_return: Any) -> Response:
        if isinstance(raw_return, Response):
            resp = raw_return
        elif isgenerator(raw_return) or isasyncgen(raw_return):
            if isgenerator(raw_return) and not isasyncgen(raw_return):
                encode_wrapper = syncgen_encode_wrapper(raw_return, self._encoder)
            else:
                encode_wrapper = agen_encode_wrapper(raw_return, self._encoder)
            resp = StreamingResponse(
                encode_wrapper,
                media_type="text/event-stream",
                status_code=self._status_code,
            )
        else:
            resp = Response(
                content=self._encoder(raw_return), status_code=self._status_code
            )
        # TODO: no longer do this by default, since we have `Empty`
        if (status := resp.status_code) < 200 or status in (204, 205, 304):
            resp.body = b""
        return resp

    async def __call__(self, scope: IScope, receive: IReceive, send: ISend) -> None:
        if self._static:  # when there is no params at all
            raw_return = await self.make_static_call(scope, receive, send)
            await self.return_to_response(raw_return)(scope, receive, send)
            return

        if self._scoped:
            async with self._graph.ascope() as resolver:
                raw_return = await self.make_call(scope, receive, send, resolver)
                await self.return_to_response(raw_return)(scope, receive, send)
        else:
            raw_return = await self.make_call(scope, receive, send, self._graph)
            return await self.return_to_response(raw_return)(scope, receive, send)
