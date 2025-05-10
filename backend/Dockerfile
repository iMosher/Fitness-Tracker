FROM python:3.9-slim

WORKDIR /app

COPY ./backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./backend /app/backend

# Set PYTHONPATH to include the /app directory
ENV PYTHONPATH=/app

CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000"]