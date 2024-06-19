from fastapi import FastAPI
import models
from database import engine
from routes.clients import app as app_clients
from routes.sale import app as app_sales
from routes.products import app as app_products
from routes.product_sales import app as app_product_sales

app = FastAPI()
models.Base.metadata.create_all(bind=engine)  # cria as tabelas e colunas no banco de dados

app.include_router(app_clients)  # incluindo as rotas de clientes
app.include_router(app_sales)  # incluindo as rotas de vendas
app.include_router(app_products)  # incluindo as rotas de produtos
app.include_router(app_product_sales)  # incluindo as rotas de vendas de produtos
