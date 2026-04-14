FROM python:3.10-slim

WORKDIR /app

COPY requirement.txt .

RUN pip install -r requirement.txt

COPY . .

CMD ["flask", "--app", "app", "run", "--host=0.0.0.0", "--port=5004"]