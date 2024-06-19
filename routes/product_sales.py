from fastapi import HTTPException, APIRouter
from database import db_dependency
import models
from data_models.product_sale import ProductSale

app = APIRouter()

@app.post("/product_sales")
async def post_product_sale(product_sale: ProductSale, db: db_dependency):
    db_product_sale = models.ProductSale(fk_product_id=product_sale.fk_product_id, fk_sale_id=product_sale.fk_sale_id, quantity=product_sale.quantity)
    db.add(db_product_sale)
    db.commit()
    return 'ProductSale inserido com sucesso'

@app.get("/product_sales")
async def get_product_sales(db: db_dependency):
    result = db.query(models.ProductSale).all()
    return result

@app.get("/product_sales/{id}")
async def get_product_sale_by_id(id: int, db: db_dependency):
    result = db.query(models.ProductSale).filter(models.ProductSale.id == id).first()
    if not result:
        raise HTTPException(status_code=404, detail="ProductSale not found")
    return result

@app.put("/product_sales/{id}")
async def put_product_sale(id: int, product_sale: ProductSale, db: db_dependency):
    db_product_sale = db.query(models.ProductSale).filter(models.ProductSale.id == id).first()
    if db_product_sale:
        db_product_sale.fk_product_id = product_sale.fk_product_id
        db_product_sale.fk_sale_id = product_sale.fk_sale_id
        db_product_sale.quantity = product_sale.quantity
        db.commit()
        return 'ProductSale atualizado com sucesso'
    
@app.delete("/product_sales/{id}")
async def delete_product_sale(id: int, db: db_dependency):
    db_product_sale = db.query(models.ProductSale).filter(models.ProductSale.id == id).first()
    if db_product_sale:
        db.delete(db_product_sale)
        db.commit()
        return 'ProductSale deletado com sucesso'
    else:
        raise HTTPException(status_code=404, detail="ProductSale not found")    