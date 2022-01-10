FROM python:3.9.7

ADD ./ /dashboard

WORKDIR /dashboard

RUN pip install -r requirements.txt

CMD ["streamlit","run","main.py"]
