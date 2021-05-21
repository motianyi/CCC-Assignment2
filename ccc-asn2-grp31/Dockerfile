FROM python:3.8.10-slim

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

# COPY . /app
# WORKDIR /app

ENV port 8887
ENV threads 2
EXPOSE 8887
COPY [".", "/"]

# copy 
RUN chmod +x /gunicorn_starter.sh; 
ENTRYPOINT ["/gunicorn_starter.sh"]


# docker rm -f web_frontend
# docker build -t web_frontend .
# docker run --name web_frontend -p 8887:8003 -d web_frontend


## push to docker hub 
# docker tag web_frontend motianyi/ccc-flask-backend:v2 
# docker push motianyi/ccc-flask-backend:v2