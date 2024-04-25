FROM python:3.12.3

WORKDIR /app

COPY requirements.txt .
COPY features ./features
COPY configurations ./configurations
COPY utilities ./utilities

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["behave"]
