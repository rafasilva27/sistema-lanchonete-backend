from pydantic import BaseModel

class Client(BaseModel):
    name: str
    phone: int
    cep: int
    address: str
    neighborhood: str
    number: int
    complement: str   