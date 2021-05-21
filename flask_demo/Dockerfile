FROM python:3.8.10-slim

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

# COPY . /app
# WORKDIR /app

ENV port 8003
ENV threads 2
EXPOSE 8003
COPY [".", "/"]

# copy 
RUN chmod +x /gunicorn_starter.sh; 
ENTRYPOINT ["/gunicorn_starter.sh"]



# docker rm -f flask_demo_app
# docker build -t flask_demo .
# docker run --name flask_demo_app -p 8888:8003 -d flask_demo