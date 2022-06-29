FROM python:3-alpine
WORKDIR /service

COPY requirements.txt .
#COPY app.py ./service
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000
ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0

ENTRYPOINT ["flask", "run"]