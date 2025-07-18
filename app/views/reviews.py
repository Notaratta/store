from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import get_session
from app import models, schemas

router = APIRouter()



@router.get("/api/review", response_model=list[schemas.Review])
async def get_reviews(db: AsyncSession = Depends(get_session)):
    reviews = await db.execute(select(models.Review)) 
    return reviews.scalars().all()

@router.post("/api/review", response_model=schemas.ReviewCreate)
async def create_review(review: schemas.ReviewCreate, db: AsyncSession = Depends(get_session)):
    db_review = models.Review(**review.dict())
    db.add(db_review)
    await db.commit()
    await db.refresh(db_review)
    return db_review 