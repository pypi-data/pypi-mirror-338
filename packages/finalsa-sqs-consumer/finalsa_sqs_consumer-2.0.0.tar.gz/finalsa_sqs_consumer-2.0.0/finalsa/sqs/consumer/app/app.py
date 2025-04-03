from finalsa.common.models import SqsReponse, AsyncMeta
from finalsa.sqs.consumer.app.signal_handler import SignalHandler
from finalsa.sqs.consumer.app.consumer import SqsConsumer
from finalsa.sqs.consumer.app.interceptors import (AsyncConsumerInterceptor,
                                                   get_handler_interceptor)
from finalsa.sqs.consumer.app.exceptions import (
    InvalidMessageException, TopicNotFoundException
)
from finalsa.sqs.consumer.app.executor import Executor
from finalsa.traceability import set_context_from_dict, get_correlation_id
from finalsa.sqs.client import (
    SqsServiceImpl, SqsService)
from finalsa.sns.client import (
    SnsClient, SnsClientImpl)
from typing import Dict, List, Callable
from datetime import datetime, timezone
from logging import getLogger, Logger
from asyncio import sleep, run
import time


class SqsApp(SqsConsumer):

    __sqs__: SqsService
    __sns__: SnsClient
    __handlers__: Dict[str, Callable]
    __interceptors__: List[AsyncConsumerInterceptor]

    def __init__(
        self,
        app_name: str = '',
        queue_url: str = '',
        max_number_of_messages: int = 1,
        workers: int = 5,
        interceptors: List[AsyncConsumerInterceptor] = []
    ) -> None:
        self.app_name = app_name
        self.sqs_url = queue_url
        self.sqs_max_number_of_messages = max_number_of_messages
        self.__handlers__: Dict[str, Callable] = {}
        self.logger: Logger = getLogger("finalsa.sqs.consumer")
        self.__signal_handler__ = SignalHandler(self.logger)
        self.workers = workers
        self.__interceptors__ = []
        for interceptor in interceptors:
            self.__interceptors__.append(interceptor())

    def run(self):
        self.__sqs__: SqsService = SqsServiceImpl()
        self.__sns__: SnsClient = SnsClientImpl()
        self.logger.info("Running consumer")
        run(self.__start__())
        self.logger.info("Consumer stopped")

    def __stop__(self):
        self.logger.info("Stopping consumer")
        self.__signal_handler__.received_signal = True

    def __subscribe__(self):
        for key in self.__handlers__:
            self.__sns__.get_or_create_topic(key)
            arn = self.__sqs__.get_queue_arn(self.sqs_url)
            if not self.__sns__.subscription_exists(key, arn):
                self.__sns__.subscribe(key, "sqs", arn)

    async def __start__(self):
        self.logger.info("Starting consumer")
        self.__subscribe__()
        while not self.__signal_handler__.received_signal:
            self.logger.debug("Receiving messages")
            await self.__receive_message__()

    async def __receive_message__(self):
        try:
            messages = self.__sqs__.receive_messages(
                queue_url=self.sqs_url,
                max_number_of_messages=self.sqs_max_number_of_messages,
                wait_time_seconds=1
            )
            if not messages or len(messages) == 0:
                await sleep(1)
                return
            self.logger.info(f"Received {len(messages)} messages")
            await self.__process_messages__(messages)

        except Exception as ex:
            self.logger.error(ex)

    async def process_message(self, message: Dict, meta: AsyncMeta):
        start_time = time.time()
        self.logger.info("Processing message", extra={
            "topic": meta.topic
        })
        await self.__process_message__(message, meta)
        end_time = time.time()
        self.logger.info(f"Message processed in {end_time-start_time} seconds", extra={
            "topic": meta.topic
        })

    async def __process_message__(self, message: Dict, meta: AsyncMeta):
        if meta.topic not in self.__handlers__:
            self.logger.error(
                f"No handler found for topic {meta.topic}")
            raise TopicNotFoundException(meta.topic)
        fn_handler = self.__handlers__[meta.topic]
        handler_interceptor = get_handler_interceptor(fn_handler)
        interceptors = []
        for interceptor in self.__interceptors__:
            interceptors.append(interceptor)
        interceptors.append(handler_interceptor())
        executor = Executor(interceptors)
        await executor.call(message, meta)

    async def __set_context_and_process_message__(self, response: SqsReponse):
        payload = response.get_payload()
        set_context_from_dict(
            response.message_attributes, self.app_name
        )
        actual_datetime = datetime.now(timezone.utc)
        meta = AsyncMeta(
            topic=response.topic,
            timestamp=actual_datetime,
            subtopic=response.message_attributes.get(
                "subtopic", None
            ),
            correlation_id=get_correlation_id(),
            produced_at=response.message_attributes.get(
                "produced_at",  actual_datetime
            ),
            consumed_at=actual_datetime,
            retry_count=response.message_attributes.get(
                "retry_count", 0
            ),
        )
        return await self.process_message(payload, meta)

    async def __process_messages__(self, messages: List[SqsReponse]):
        for message in messages:
            try:
                await self.__set_context_and_process_message__(message)
                self.__sqs__.delete_message(
                    self.sqs_url, message.receipt_handle)
            except InvalidMessageException as ex:
                self.logger.error("Invalid message received")
                self.logger.exception(ex)
            except Exception as ex:
                self.logger.error("Error processing message", extra={
                    "message_id": message.message_id
                })
                self.logger.exception(ex)
