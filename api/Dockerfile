FROM python:3.9.7

ADD ./ /api

WORKDIR /api

RUN pip install -r requirements.txt

CMD ["sh", "-c","uvicorn main:app --host 0.0.0.0 --port $PORT"]
