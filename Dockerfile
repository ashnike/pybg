# Build environment
FROM python:3.9-alpine as builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime environment
FROM python:3.9-alpine

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/
COPY --from=builder /usr/local/bin /usr/local/bin

COPY . .


# EXPOSE port for Flask
EXPOSE 5000

# Use gunicorn to run the Flask app
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"] 

