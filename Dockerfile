# Use official Python image
FROM python:3.11-slim

WORKDIR /app

# Install pip tools
RUN pip install --upgrade pip

# Copy requirements (if exists)
COPY requirements.txt ./
RUN pip install -r requirements.txt || true

# Or use pyproject.toml if exists
COPY pyproject.toml ./
RUN pip install . || true

# Copy the rest of the code
COPY . .

# Expose port
EXPOSE 8000

# Run migrations and start the app
CMD alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload 