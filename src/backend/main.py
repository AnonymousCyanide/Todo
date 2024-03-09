from fastapi import FastAPI , HTTPException
from models import Todo , TodoListResponse , SaveTodo
from database import add_todo_to_db ,get_all_todo_from_db , get_todo_by_id , delete_todo_in_db
app = FastAPI()

dummy_db =[]


@app.get("/")
async def root():
    return {"message": "Hello World"}

# Get all Todos
@app.get("/todos" , status_code=200 , response_model=TodoListResponse)
def get_all_todos():
    response = {"todos":get_all_todo_from_db()}
    return response

# Get Single Todo
@app.get("/todo/{id}" , status_code=200 , response_model=Todo)
def get_todo(id : str):

    response = get_todo_by_id(id)
    return response

# Save todo
@app.post("/todo" , status_code=200 )
async def add_todo(todo :SaveTodo ):
    try:
        add_todo_to_db(todo)
        return {"message":"Added Successfully"}
    except :
       return  HTTPException(status_code=400 , detail="Something went wrong")
    

# Delete Todo
@app.delete("/todo/{id}" , status_code=202)
def delete_todo(id : str):
    delete_todo_in_db(id)
    return{"message" : "Successfully Deleted"}

