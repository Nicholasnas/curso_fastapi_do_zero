from fastapi import FastAPI, HTTPException

from fast_zero.schemas import Message, UserDB, UserList, UserPublic, UserSchema

app = FastAPI()

database = []


@app.get('/users/', response_model=UserList)
async def retorna_usuarios():
    return {'users': database}


@app.post('/users/', status_code=201, response_model=UserPublic)
async def criar_usuario(user: UserSchema):
    usuario_id = UserDB(**user.model_dump(), id=len(database) + 1)

    database.append(usuario_id)

    return usuario_id


@app.put('/users/{user_id}', response_model=UserPublic, status_code=200)
async def put_usuario(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(status_code=404, detail='User não encontrado')

    usuario_id = UserDB(**user.model_dump(), id=user_id)
    database[user_id - 1] = usuario_id
    return usuario_id


@app.delete('/users/{user_id}', response_model=Message)
async def delete_usuario(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(status_code=404, detail='User não encontrado')

    del database[user_id - 1]
    return {'detail': 'User deleted'}
