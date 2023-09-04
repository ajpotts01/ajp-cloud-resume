FROM python:3.9.17-slim

WORKDIR /application

COPY . /application

RUN apt-get update && apt-get -y install wget

RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN wget https://github.com/benbjohnson/litestream/releases/download/v0.3.9/litestream-v0.3.9-linux-amd64.deb

RUN dpkg -i litestream-v0.3.9-linux-amd64.deb

EXPOSE 8080

ENV ENVIRONMENT=GCR

#CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8080"]
# https://medium.com/harvested-financial-engineering/deploying-a-containerized-django-gunicorn-server-on-google-cloud-run-feb13823f7f4
CMD ["sh", "-c", "/application/start_app.sh"]