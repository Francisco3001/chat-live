FROM python:3.10.12-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
COPY . /app

RUN apt-get update && \
    apt-get install -y libpq-dev gcc

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 3001

CMD ["python", "run.py"]
#docker run -p 5000:5000 flask-app
