from fastapi import HTTPException, APIRouter
from database import db_dependency
import models
from data_models.sale import Sale

app = APIRouter()

@app.post("/sales")
async def post_sale(sale: Sale, db: db_dependency):
    db_sale = models.Sale(fk_client_id=sale.fk_client_id, date=sale.date, total=sale.total)
    db.add(db_sale)
    db.commit()
    return 'Venda inserida com sucesso'

@app.get("/sales")
async def get_sales(db: db_dependency):
    result = db.query(models.Sale).all()
    return result

@app.get("/sales/{id}")
async def get_sale_by_id(id: int, db: db_dependency):
    result = db.query(models.Sale).filter(models.Sale.id == id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Sale not found")
    return result

@app.put("/sales/{id}")
async def put_sale(id: int, sale: Sale, db: db_dependency):
    db_sale = db.query(models.Sale).filter(models.Sale.id == id).first()
    if db_sale:
        db_sale.fk_client_id = sale.fk_client_id
        db_sale.date = sale.date
        db_sale.total = sale.total
        db.commit()
        return 'Venda atualizada com sucesso'
    else:
        raise HTTPException(status_code=404, detail="Sale not found")

@app.delete("/sales/{id}")
async def delete_sale(id: int, db: db_dependency):
    db_sale = db.query(models.Sale).filter(models.Sale.id == id).first()
    if db_sale:
        db.delete(db_sale)
        db.commit()
        return 'Venda deletada com sucesso'
    else:
        raise HTTPException(status_code=404, detail="Sale not found")