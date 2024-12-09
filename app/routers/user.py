# В модуле user.py напишите APIRouter с префиксом '/user' и тегом 'user', а также следующие маршруты, с пустыми функциями:
# get '/' с функцией all_users.
# get '/user_id' с функцией user_by_id.
# post '/create' с функцией create_user.
# put '/update' с функцией update_user.
# delete '/delete' с функцией delete_user.

# Подготовьтесь и импортируйте все необходимые классы и функции (ваши пути могут отличаться):
from fastapi import APIRouter, Depends, status, HTTPException
# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from app.backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated
from app.models.user import User
from app.schemas import CreateUser, UpdateUser
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify


from fastapi import FastAPI, APIRouter

router=APIRouter(prefix="/user",tags=["user"])
DbSession = Annotated[Session, Depends(get_db)]

# Напишите логику работы функций маршрутов:
# Каждая из нижеперечисленных функций подключается к базе данных в момент обращения при помощи функции
# get_db - Annotated[Session, Depends(get_db)]

# Функция all_users ('/'):
# Должна возвращать список всех пользователей из БД. Используйте scalars, select и all

@router.get("/")
async def all_users(db: DbSession):
    users = db.scalars(select(User)).all()
    return users

# Функция user_by_id ('/user_id'):
# Для извлечения записи используйте ранее импортированную функцию select.
# Дополнительно принимает user_id.
# Выбирает одного пользователя из БД.
# Если пользователь не None, то возвращает его.
# В противном случае выбрасывает исключение с кодом 404 и описанием "User was not found"


@router.get("/{user_id}")
async def by_id(db: DbSession, user_id: int):
    by_id_users = db.scalars(select(User).where(User.id == user_id)).all()
    if by_id_users is  None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User was not found")
    return by_id_users

# Функция craete_user ('/create'):
# Для добавления используйте ранее импортированную функцию insert.
# Дополнительно принимает модель CreateUser.
# Подставляет в таблицу User запись значениями указанными в CreateUser.
# В конце возвращает словарь {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}
# Обработку исключения существующего пользователя по user_id или username можете сделать по желанию.

@router.post("/create")
async def create_user(db: DbSession, create_user: CreateUser):

    db.execute(insert(User).values(username=create_user.username,
                                   firstname=create_user.firstname,
                                   lastname=create_user.lastname,
                                   age=create_user.age))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


# Функция update_user ('/update'):
# Для обновления используйте ранее импортированную функцию update.
# Дополнительно принимает модель UpdateUser и user_id.
# Если находит пользователя с user_id, то заменяет эту запись значениям из модели UpdateUser.
# Далее возвращает словарь {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}
# В противном случае выбрасывает исключение с кодом 404 и описанием "User was not found"

@router.put("/update")
async def update_user(db: DbSession, user_id:int, upd_user: UpdateUser):
    check_id = db.scalars(select(User).where(User.id == user_id))
    if check_id is None:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User was not found"
        )
    db.execute(update(User).where(User.id == user_id).values(
                                firstname=upd_user.firstname,
                                lastname=upd_user.lastname,
                                age=upd_user.age))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}

# Функция delete_user ('/delete'):
# Для удаления используйте ранее импортированную функцию delete.
# Всё должно работать аналогично функции update_user, только объект удаляется.
# Исключение выбрасывать то же.

@router.delete("/delete")
async def delete_user(db: DbSession, user_id:int, upd_user: UpdateUser):
    check_id = db.scalars(select(User).where(User.id == user_id))
    if check_id is None:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User was not found"
        )
    db.execute(delete(User).where(User.id == user_id).values(
                                firstname=upd_user.firstname,
                                lastname=upd_user.lastname,
                                age=upd_user.age))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}
