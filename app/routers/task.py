# В модуле task.py напишите APIRouter с префиксом '/task' и тегом 'task', а также следующие маршруты, с пустыми функциями:
# get '/' с функцией all_tasks.
# get '/task_id' с функцией task_by_id.
# post '/create' с функцией create_task.
# put '/update' с функцией update_task.
# delete '/delete' с функцией delete_task.

from fastapi import FastAPI, APIRouter

router=APIRouter(prefix="/task",tags=["task"])

@router.get("/")
async def all_tasks():
    pass
@router.get("/task_id")
async def task_by_id():
    pass

@router.post("/create")
async def create_task():
    pass

@router.put("/update")
async def update_task():
    pass

@router.delete("/delete")
async def delete_task():
    pass