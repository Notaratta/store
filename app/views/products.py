from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app import schemas
from app.models import Product as ProductModel, Order as OrderModel
from app.database import get_session
from app.email_utils import send_order_confirmation_email

router = APIRouter()

@router.get("/api/products", response_model=list[schemas.Product])
async def get_products(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(ProductModel))
    products = result.scalars().all()
    return products

@router.post("/api/products", response_model=schemas.Product)
async def create_products(product:schemas.ProductCreate, session: AsyncSession = Depends(get_session)):
    product = ProductModel(**product.dict())
    session.add(product)
    await session.commit()
    await session.refresh(product)
    return product

@router.post("/api/orders", response_model=schemas.Order)
async def create_order(order: schemas.OrderCreate, session: AsyncSession = Depends(get_session)):
    db_order = OrderModel(**order.dict())
    session.add(db_order)
    await session.commit()
    await session.refresh(db_order)
    send_order_confirmation_email.delay(db_order.email,  db_order.status, db_order.product_id)
    return db_order




# @router.get("/product/{product_id}")
# def get_product(product_id: int):
#     product = next((p for p in products if p["id"] == product_id), None)
#     if not product:
#         return JSONResponse(status_code=404, content={"error": "Product not found"})
#     return product 