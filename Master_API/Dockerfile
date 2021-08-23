FROM python:3.9.1-slim-buster

COPY ./ /app/
WORKDIR /app/
RUN pip3 install -r ./requierment.txt
EXPOSE 5000
ENV FLASK_APP=/app/main.py

CMD flask run --host=0.0.0.0 --port=5000
