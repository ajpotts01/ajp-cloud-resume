FROM python:3.9.17-slim

WORKDIR /application

COPY . /application

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8080

ENV ENVIRONMENT=GCR

RUN python manage.py migrate
RUN python manage.py collectstatic --verbosity 2 --no-input

#CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8080"]
# https://medium.com/harvested-financial-engineering/deploying-a-containerized-django-gunicorn-server-on-google-cloud-run-feb13823f7f4
CMD ["sh", "-c", "gunicorn --preload cloud_resume.wsgi:application --bind 0.0.0.0:8080"]