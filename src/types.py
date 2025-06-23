from typing import Dict
from typing import Literal
from typing import TypedDict
from typing import Union


class Operation(TypedDict):
    id: int
    state: Literal["EXECUTED", "PENDING", "CANCELED"]
    date: str
    operationAmount: Dict[str, Union[str, Dict[str, str]]]
    description: str
    from_: str
    to: str
