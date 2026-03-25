
# -------- STAGE 1: Builder --------
FROM python:3.10-alpine AS builder

WORKDIR /app

# Instalar dependencias necesarias para compilar extensiones
RUN apk add --no-cache \
    build-base \
    linux-headers \
    libffi-dev \
    openssl-dev

# Copiar requerimientos e instalarlos en un directorio aislado
COPY requirements.txt .

COPY . .


RUN pip install --prefix=/install --no-cache-dir -r requirements.txt


# -------- STAGE 2: Runtime --------
FROM python:3.10-alpine

WORKDIR /app

# Instalar librerías mínimas necesarias en runtime
RUN apk add --no-cache \
    libstdc++ \
    libffi \
    openssl

# Copiar dependencias del builder
COPY --from=builder /install /usr/local

# Copiar aplicación
COPY . .

# Exponer puerto de Gunicorn
EXPOSE 5000

# Ejecutar con Gunicorn (usa tu archivo app.py con variable app = Flask(...))
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
