from pydantic import BaseModel , Field , BeforeValidator 
from typing import List ,Optional, Annotated

PyObjectId = Annotated[str, BeforeValidator(str)]

class Todo(BaseModel):
    id : Optional[PyObjectId] = Field(alias="_id" , default=None)
    title : str
    description : str

class SaveTodo(BaseModel):
    title : str
    description : str
    
class TodoListResponse(BaseModel):
    todos : List[Todo]