# В модуле user.py напишите APIRouter с префиксом '/user' и тегом 'user', а также следующие маршруты, с пустыми функциями:
# get '/' с функцией all_users.
# get '/user_id' с функцией user_by_id.
# post '/create' с функцией create_user.
# put '/update' с функцией update_user.
# delete '/delete' с функцией delete_user.

from fastapi import FastAPI, APIRouter

router=APIRouter(prefix="/user",tags=["user"])

@router.get("/")
async def all_users():
    pass
@router.get("/user_id")
async def by_id():
    pass

@router.post("/create")
async def create_user():
    pass

@router.put("/update")
async def update_user():
    pass

@router.delete("/delete")
async def delete_user():
    pass