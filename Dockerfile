FROM python:alpine3.7
LABEL version="1.0"
ADD ./src /app
WORKDIR /app
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 8000
RUN /bin/sh startup.sh
RUN rm startup.sh
CMD gunicorn linkr.wsgi:application --bind 0.0.0.0:8000 --workers 3
