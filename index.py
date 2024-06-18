from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Annotated
from data_models.client import Client
from data_models.product import Product
from data_models.product_sale import ProductSale
from data_models.sale import Sale
import models
from database import engine
from sqlalchemy.orm import Session
from routes.clients import app as app_clients
from routes.sale import app as app_sales

app = FastAPI()
models.Base.metadata.create_all(bind=engine)  # cria as tabelas e colunas no banco de dados

app.include_router(app_clients)  # incluindo as rotas de clientes
app.include_router(app_sales)  # incluindo as rotas de vendas
