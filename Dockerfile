FROM python:alpine3.7
LABEL version="1.0"

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD ./src /app
WORKDIR /app
COPY requirements.txt ./

# RUN export PATH=/usr/lib/postgresql/X.Y/bin/:$PATH
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 pip install --upgrade pip setuptools && \
 pip install --upgrade pip setuptools && \
 pip install -r requirements.txt --no-cache-dir

# RUN pip install --upgrade pip setuptools && pip install -r requirements.txt
EXPOSE 8000

# RUN /bin/sh startup.sh
# RUN rm startup.sh

CMD gunicorn linkr.wsgi:application --bind 0.0.0.0:8000 --workers 3