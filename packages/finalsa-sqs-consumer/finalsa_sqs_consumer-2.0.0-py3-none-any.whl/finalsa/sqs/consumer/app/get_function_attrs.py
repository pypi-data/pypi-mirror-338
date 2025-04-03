from finalsa.sqs.consumer.app.base_model_attr import base_model_attr
from finalsa.sqs.consumer.app.dict_model_attr import dict_model_attr
from finalsa.common.models import AsyncMeta
from typing import Any, Dict


def get_function_attrs(
    message: Dict,
    meta: AsyncMeta,
    func_attrs: Dict[str, Any] = None,
) -> Dict[str, Any]:
    attrs_to_insert = {}
    if 'timestamp' in func_attrs:
        attrs_to_insert['timestamp'] = meta.timestamp
    if 'correlation_id' in func_attrs:
        attrs_to_insert['correlation_id'] = meta.correlation_id
    if 'meta' in func_attrs:
        attrs_to_insert['meta'] = meta
    base_model = base_model_attr(func_attrs)
    if base_model:
        attrs_to_insert[base_model[0]] = base_model[1](**message)
    dict_model = dict_model_attr(func_attrs)
    if dict_model:
        attrs_to_insert[dict_model[0]] = message
    return attrs_to_insert
