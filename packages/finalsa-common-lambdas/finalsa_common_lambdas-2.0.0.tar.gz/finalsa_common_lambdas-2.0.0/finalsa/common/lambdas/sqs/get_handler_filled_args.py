from finalsa.common.lambdas.sqs.SqsEvent import SqsEvent
from finalsa.common.models import Meta
from typing import Union, Dict, Any
from pydantic import BaseModel


def get_handler_filled_args(
    attrs: Dict[str, Any],
    payload: Union[Dict, str],
    parsed_event: SqsEvent,
    meta: Meta,
) -> Dict:
    filled_args = {}
    for key, value in attrs.items():
        if key == 'return':
            continue
        if isinstance(value, type):
            if issubclass(value, SqsEvent):
                filled_args[key] = parsed_event
                continue
            elif value == Meta:
                filled_args[key] = meta
                continue
            elif issubclass(value, BaseModel):
                filled_args[key] = value(**payload)
                continue
        if key == "meta":
            filled_args[key] = meta
        if key == "message":
            filled_args[key] = payload
        elif key in payload:
            filled_args[key] = payload[key]
    return filled_args
