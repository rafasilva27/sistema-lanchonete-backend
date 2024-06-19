from fastapi import FastAPI
import models
from database import engine
from routes.clients import app as app_clients
from routes.sale import app as app_sales

app = FastAPI()
models.Base.metadata.create_all(bind=engine)  # cria as tabelas e colunas no banco de dados

app.include_router(app_clients)  # incluindo as rotas de clientes
app.include_router(app_sales)  # incluindo as rotas de vendas
