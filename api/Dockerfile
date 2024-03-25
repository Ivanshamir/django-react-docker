FROM python:3.12-slim-bullseye

# set work directory
WORKDIR /src/api

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .

RUN apt-get update && apt-get install -y \
  build-essential \
  gcc \
  netcat \
  libpq-dev \
  default-libmysqlclient-dev \
  python3-dev \
  pkg-config \
  && apt-get clean

# install temp dependencies for build of pyscopg2 etc
RUN pip install gunicorn
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project
COPY . .

RUN sed -i 's/\r$//g' /src/api/entrypoint.sh
RUN chmod +x /src/api/entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/src/api/entrypoint.sh"]