from finalsa.common.models import Meta
from abc import ABC, abstractmethod
from typing import Callable, Dict


class AsyncConsumerInterceptor(ABC):

    @abstractmethod
    async def __call__(self, message: Dict, meta: Meta, call_next: Callable) -> Dict:
        pass


def get_handler_interceptor(fn_handler) -> Callable[[Callable], AsyncConsumerInterceptor]:
    class HandlerInterceptor(AsyncConsumerInterceptor):
        async def __call__(self, message, meta, _):
            await fn_handler(message, meta)

    return HandlerInterceptor
