# Hello API - Tutorial Avançado

API RESTful desenvolvida com FastAPI, Docker e UV para estudantes avançados do LAB365.

## Tecnologias Utilizadas

- **FastAPI**: Framework moderno para construção de APIs
- **Docker**: Containerização da aplicação
- **UV**: Gerenciador de pacotes Python rápido
- **Uvicorn**: Servidor ASGI de alta performance
- **Swagger/OpenAPI**: Documentação automática da API

## Estrutura do Projeto

```
hello-api/
├── app/
│   └── main.py          # Código principal da API
├── Dockerfile            # Configuração do container
├── docker-compose.yml    # Orquestração do Docker
├── pyproject.toml        # Dependências do projeto (UV)
├── .dockerignore         # Arquivos ignorados pelo Docker
└── README.md            # Este arquivo
```

## Endpoints da API

A API possui 5 endpoints principais:

### 1. GET `/` - Root
Retorna mensagem de boas-vindas

### 2. GET `/users` - Listar Usuários
Retorna todos os usuários cadastrados

### 3. GET `/users/{user_id}` - Buscar Usuário
Retorna um usuário específico pelo ID

### 4. POST `/users` - Criar Usuário
Cria um novo usuário no sistema

### 5. GET `/health` - Health Check
Verifica o status da API

## Pré-requisitos

- [Docker](https://www.docker.com/get-started) instalado
- [Docker Compose](https://docs.docker.com/compose/install/) instalado
- Git para clonar o repositório

## Como Executar o Projeto

### Passo 1: Clone o Repositório

```bash
git clone https://github.com/IA-para-DEVs-SD/hello-api.git
cd hello-api
```

### Passo 2: Build e Execute com Docker Compose

```bash
docker-compose up --build
```

Este comando irá:
- Construir a imagem Docker
- Instalar as dependências usando UV
- Iniciar o container
- Expor a API na porta 8000

### Passo 3: Acesse a API

Após a inicialização, a API estará disponível em:

- **API**: http://localhost:8000
- **Documentação Swagger**: http://localhost:8000/docs
- **Documentação ReDoc**: http://localhost:8000/redoc

## Testando os Endpoints

### Via Swagger UI (Recomendado)

1. Acesse http://localhost:8000/docs
2. Experimente os endpoints diretamente pela interface

### Via cURL

#### Listar todos os usuários
```bash
curl http://localhost:8000/users
```

#### Buscar usuário específico
```bash
curl http://localhost:8000/users/1
```

#### Criar novo usuário
```bash
curl -X POST http://localhost:8000/users \
  -H "Content-Type: application/json" \
  -d '{"id": 3, "name": "Pedro Costa", "email": "pedro@example.com"}'
```

#### Health check
```bash
curl http://localhost:8000/health
```

## Desenvolvimento Local (Sem Docker)

Se preferir executar sem Docker:

### 1. Instale o UV

```bash
# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Linux/macOS
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Instale as Dependências

```bash
uv pip install -r pyproject.toml
```

### 3. Execute a API

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Comandos Úteis do Docker

### Parar a aplicação
```bash
docker-compose down
```

### Ver logs
```bash
docker-compose logs -f
```

### Rebuild da imagem
```bash
docker-compose up --build
```

### Remover containers e volumes
```bash
docker-compose down -v
```

## Próximos Passos

Experimente modificar a API:

1. Adicione novos endpoints
2. Implemente validações mais complexas
3. Adicione um banco de dados (PostgreSQL, MongoDB)
4. Implemente autenticação JWT
5. Adicione testes automatizados

## Exercício Prático

1. Clone este repositório
2. Execute a aplicação com Docker
3. Teste todos os endpoints via Swagger
4. Adicione um novo endpoint `DELETE /users/{user_id}`
5. Adicione validação de e-mail no modelo User
6. Faça commit e push das suas alterações

## Recursos Adicionais

- [Documentação FastAPI](https://fastapi.tiangolo.com/)
- [Documentação Docker](https://docs.docker.com/)
- [Documentação UV](https://docs.astral.sh/uv/)
- [Tutorial Docker para Python](https://docs.docker.com/language/python/)

## Suporte

Para dúvidas e problemas, abra uma issue no repositório.

---

Desenvolvido para o curso **IA para DEVs [SD]** - LAB365 / SENAI
