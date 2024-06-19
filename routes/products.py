from fastapi import HTTPException, APIRouter
from database import db_dependency
import models
from data_models.product import Product

app = APIRouter()

@app.post("/products")
async def post_product(product: Product, db: db_dependency):
    db_product = models.Product(name=product.name, description=product.description, price=product.price, stock=product.stock)
    db.add(db_product)
    db.commit()
    return 'Produto inserido com sucesso'

@app.get("/products")
async def get_products(db: db_dependency):
    result = db.query(models.Product).all()
    return result

@app.get("/products/{id}")
async def get_product_by_id(id: int, db: db_dependency):
    result = db.query(models.Product).filter(models.Product.id == id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Product not found")
    return result

@app.put("/products/{id}")
async def put_product(id: int, product: Product, db: db_dependency):
    db_product = db.query(models.Product).filter(models.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.stock = product.stock
        db.commit()
        return 'Produto atualizado com sucesso'
    else:
        raise HTTPException(status_code=404, detail="Product not found")

@app.delete("/products/{id}")
async def delete_product(id: int, db: db_dependency):
    db_product = db.query(models.Product).filter(models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return 'Produto deletado com sucesso'
    else:
        raise HTTPException(status_code=404, detail="Product not found")