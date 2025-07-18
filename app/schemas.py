from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    cons: list[str] = []
    class Config:
        from_attributes = True

class ProductCreate(BaseModel):
    name: str
    price: float
    cons: list[str] = []
    class Config:
        from_attributes = True

class ReviewCreate(BaseModel):
    name: str
    rating: float
    text: str
    class Config:
        from_attributes = True

class Review(ReviewCreate):
    id: int
    class Config:
        from_attributes = True 

# schemas.py
class OrderCreate(BaseModel):
    email: str
    password: str
    product_id: int

class Order(BaseModel):
    id: int
    email: str
    password: str
    product_id: int
    created_at: str
    class Config:
        from_attributes = True