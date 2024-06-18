from fastapi import HTTPException, APIRouter
from database import db_dependency
import models
from data_models.client import Client

app = APIRouter()

@app.post("/clients")
async def post_client(client: Client, db: db_dependency):
    db_client = models.Client(name=client.name, phone=client.phone, cep=client.cep, address=client.address, neighborhood=client.neighborhood, number=client.number, complement=client.complement)
    db.add(db_client)
    db.commit()
    return 'Cliente inserido com sucesso'

@app.get("/clients")
async def get_clients(db: db_dependency):
    result = db.query(models.Client).all()
    return result


@app.get("/clients/{id}")
async def get_client_by_id(id: int, db: db_dependency):
    result = db.query(models.Client).filter(models.Client.id == id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Client not found")
    return result

@app.put("/clients/{id}")
async def put_client(id: int, client: Client, db: db_dependency):
    db_client = db.query(models.Client).filter(models.Client.id == id).first()
    if db_client:
        db_client.name = client.name
        db_client.phone = client.phone
        db_client.cep = client.cep
        db_client.address = client.address
        db_client.neighborhood = client.neighborhood
        db_client.number = client.number
        db_client.complement = client.complement
        db.commit()
        return 'Cliente atualizado com sucesso'
    else:
        raise HTTPException(status_code=404, detail="Client not found")
    
@app.delete("/clients/{id}")
async def delete_client(id: int, db: db_dependency):
    db_client = db.query(models.Client).filter(models.Client.id == id).first()
    if db_client:
        db.delete(db_client)
        db.commit()
        return 'Cliente deletado com sucesso'
    else:
        raise HTTPException(status_code=404, detail="Client not found")
    