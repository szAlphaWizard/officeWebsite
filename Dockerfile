FROM python:3.6
WORKDIR /app
COPY requirements.txt /app/
ADD . /app
RUN apt-get update && apt-get install MySQL-client-core-5.7 mysql-client-5.7 && rm -rf /var/lib/apt/lists/*
RUN pip install -i https://pypi.doubanio.com/simple/ -r requirements.txt
EXPOSE 80