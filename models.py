from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float
from database import Base

# criando as tabelas no banco de dados
class Client(Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone = Column(Integer)
    cep = Column(Integer)
    address = Column(String)
    neighborhood = Column(String)
    number = Column(Integer)
    complement = Column(String)

class ProductSale(Base):
    __tablename__ = "product_sale"

    id = Column(Integer, primary_key=True, index=True)
    fk_product_id = Column(Integer, ForeignKey("product.id"))
    fk_sale_id = Column(Integer, ForeignKey("sale.id"))
    quantity = Column(Integer)

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    stock = Column(Integer)

class Sale(Base):
    __tablename__ = "sale"

    id = Column(Integer, primary_key=True, index=True)
    fk_client_id = Column(Integer, ForeignKey("client.id"))
    date = Column(DateTime)
    total = Column(Float)