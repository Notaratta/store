from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
from app import models
from app.views import reviews, pages, products
import uvicorn
app = FastAPI(debug=True)

# Enable CORS for frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
static_dir = os.path.join(os.path.dirname(__file__), '../static')
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Create tables

# Routers
app.include_router(pages.router)
app.include_router(products.router)
app.include_router(reviews.router)

# if __name__ == "__main__":
#     uvicorn.run(app, debug=True)