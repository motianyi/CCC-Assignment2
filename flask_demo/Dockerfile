FROM python:3.8.10-slim

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

# COPY . /app
# WORKDIR /app
COPY [".", "/"]
RUN chmod +x /gunicorn_starter.sh; 
ENTRYPOINT ["/gunicorn_starter.sh"]