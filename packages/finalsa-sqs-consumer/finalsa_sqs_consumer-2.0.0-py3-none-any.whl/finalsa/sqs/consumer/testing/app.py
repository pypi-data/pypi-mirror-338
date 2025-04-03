from finalsa.traceability.context import set_context_from_dict, get_correlation_id
from finalsa.sqs.client import SqsServiceTest
from finalsa.sns.client import SnsClientTest
from finalsa.common.models import AsyncMeta
from finalsa.sqs.consumer.app import SqsApp
from asyncio import run
from typing import Any, Optional
from datetime import datetime, timezone


class SqsAppTest():

    def __init__(self, app: SqsApp) -> None:
        self.app = app

    def consume(
        self,
        topic: str,
        payload: Any,
        timestamp: Optional[datetime] = None,
        meta: Optional[AsyncMeta] = None,
    ):
        self.app.__sqs__ = SqsServiceTest()
        self.app.__sns__ = SnsClientTest()
        correlation_id = f"test-{topic}"
        set_context_from_dict(
            {"correlation_id": correlation_id}, self.app.app_name)
        if not timestamp:
            timestamp = datetime.now(timezone.utc)
        if not meta:
            meta = AsyncMeta(
                topic=topic,
                timestamp=timestamp,
                correlation_id=get_correlation_id(),
                produced_at=datetime.now(timezone.utc),
                consumed_at=datetime.now(timezone.utc)
            )
        run(self.app.process_message(payload, meta))
