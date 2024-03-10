from models import Todo , SaveTodo
from bson.objectid import ObjectId
from pymongo import MongoClient

pwd = ''

client = MongoClient(f"mongodb+srv://avidubey2000:{pwd}@cluster0.o3scw1k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

database = client.TodoApp
collection = database.todo


def add_todo_to_db(todo : SaveTodo):
    #print(collection.find().limit(5))
    collection.insert_one(todo.model_dump())

def get_all_todo_from_db():
    todos = list(collection.find())

    return todos

def get_todo_by_id(id : str):

    todo = collection.find_one({"_id" : ObjectId(id)})

    return todo

def delete_todo_in_db(id : str):
    collection.delete_one({"_id":ObjectId(id)})