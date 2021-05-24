FROM python:3.8.10-slim

#COPY requirements.txt /
#RUN pip3 install -r /requirements.txt

# COPY . /app
# WORKDIR /app
ENV http_proxy http://wwwproxy.unimelb.edu.au:8000/
ENV https_proxy http://wwwproxy.unimelb.edu.au:8000/
ENV HTTP_PROXY http://wwwproxy.unimelb.edu.au:8000/
ENV HTTPS_PROXY http://wwwproxy.unimelb.edu.au:8000/
ENV no_proxy localhost,127.0.0.1,localaddress,172.16.0.0/12,.melbourne.rc.nectar.org.au,.storage.u nimelb.edu.au,.cloud.unimelb.edu.au

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

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
