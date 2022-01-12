FROM python:3.9.7

ADD ./ /dashboard

WORKDIR /dashboard

RUN pip install -r requirements.txt

CMD ["sh","-c","streamlit run --server.port $PORT main.py"]
