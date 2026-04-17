FROM python:3.10-slim
WORKDIR /app
COPY . .
# This will run your delivery logic
CMD ["python", "delivery.py"]
