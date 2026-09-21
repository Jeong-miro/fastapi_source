from datetime import datetime

from pydantic import BaseModel, PositiveInt,ValidationError
from typing import Annotated, Literal
from annotated_types import Gt
from pydantic import StringConstraints
from pydantic import Field
from annotated_types import Ge, Le

# todo 1 개 
class TodoItem(BaseModel):
    id: int
    title: str
    completed: bool
    important: bool