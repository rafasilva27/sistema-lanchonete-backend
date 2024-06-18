from pydantic import BaseModel

class ProductSale(BaseModel):
    fk_product_id: int
    fk_sale_id: int
    quantity: int