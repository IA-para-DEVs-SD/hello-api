from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Hello API",
    description="API tutorial para estudantes avançados - LAB365",
    version="1.0.0"
)

# Modelo de dados para usuário
class User(BaseModel):
    id: int
    name: str
    email: str

# Banco de dados simulado
users_db: List[User] = [
    User(id=1, name="João Silva", email="joao@example.com"),
    User(id=2, name="Maria Santos", email="maria@example.com"),
]

# Contador para IDs
next_id = 3


@app.get("/", tags=["Root"])
def read_root():
    """
    Endpoint raiz - Retorna mensagem de boas-vindas
    """
    return {
        "message": "Bem-vindo à Hello API!",
        "docs": "/docs",
        "version": "1.0.0"
    }


@app.get("/users", response_model=List[User], tags=["Users"])
def get_users():
    """
    Retorna todos os usuários cadastrados
    """
    return users_db


@app.get("/users/{user_id}", response_model=User, tags=["Users"])
def get_user(user_id: int):
    """
    Retorna um usuário específico pelo ID
    """
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="Usuário não encontrado")


@app.post("/users", response_model=User, status_code=201, tags=["Users"])
def create_user(user: User):
    """
    Cria um novo usuário
    """
    global next_id

    # Verifica se o ID já existe
    for existing_user in users_db:
        if existing_user.id == user.id:
            raise HTTPException(status_code=400, detail="ID já existe")

    # Se o ID não foi fornecido, usa o próximo ID disponível
    if user.id == 0:
        user.id = next_id
        next_id += 1

    users_db.append(user)
    return user


@app.get("/health", tags=["Health"])
def health_check():
    """
    Verifica o status da API
    """
    return {
        "status": "healthy",
        "total_users": len(users_db)
    }
