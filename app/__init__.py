from celery import Celery

celery_app = Celery(
    'store',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)

from . import email_utils  # Ensure tasks are registered
from app.database import Base
from app.models import Review, Product