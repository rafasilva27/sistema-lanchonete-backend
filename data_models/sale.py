from pydantic import BaseModel
from datetime import date

class Sale(BaseModel):
    fk_client_id: int
    date: date
    total: int