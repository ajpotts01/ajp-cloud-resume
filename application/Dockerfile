FROM python:3.9.17-slim

WORKDIR /application

COPY . /application

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]