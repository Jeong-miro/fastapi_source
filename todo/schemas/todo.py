from datetime import datetime

from pydantic import BaseModel, PositiveInt,ValidationError ,ConfigDict
from typing import Annotated, Literal,List
from annotated_types import Gt
from pydantic import StringConstraints
from pydantic import Field
from annotated_types import Ge, Le

# 화면단과 서버단이 데이터 주고 받을 때 사용
# API 요청/응답 데이터 구조

class TodoCreate(BaseModel):
    """
    Todo 입력 요청
    """
    title: str
    completed: bool=False
    important: bool=False

class TodoUpdate(BaseModel):
    """
    Todo 수정 요청
    """
    title: str|None=None
    completed: bool|None=None
    important: bool|None=None

class TodoResponse(TodoCreate):
    """
    Todo 응답
    """
    id:int
    created_at:datetime
    updated_at:datetime

class TodoPageResponse(BaseModel):
    """
    페이지 나누기 후 리스트 조회
    """
    items:list[TodoResponse]
    total:int
    total_pages:int
    page:int
    size:int
    completed:bool | None



# todo 1 개 
# class TodoItem(BaseModel):
#     id: int
#     title: str
#     completed: bool
#     important: bool

# class Todo(BaseModel):
#     #todos:list[TodoItem]
#     todos:List[TodoItem]

#     # Swagger/OpenAPI 문서에 보여줄 환경설정
#     model_config =ConfigDict(
#         json_schema_extra={
#             "example":{
#                 "todos":[
#                     {
#                         "id": 0,
#                         "title": "sample title",
#                         "completed": True,
#                         "important": False
#                     },
#                 ]
#             }
#         }
#     )