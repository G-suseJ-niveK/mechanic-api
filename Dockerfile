FROM python:3.8

WORKDIR /app/log-api

ENV WORKDIR /app/log-api

# Copiar fuente de Lambda
COPY . .

RUN apt-get -y update
RUN python -m pip install --upgrade pip
RUN python -m pip install uvicorn

# Instalación de paquetes en packages/
RUN pip install -r ./requirements.txt
CMD ["uvicorn", "api:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]
