FROM python:alpine
MAINTAINER RastiTheWolf (app) root@bonn333.eu (dockerization)
ENV PYTHONNUNBUFFERED 1
RUN mkdir /furrystar
WORKDIR /furrystar
COPY requirements.txt /furrystar/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /furrystar/
EXPOSE 2137
CMD ["python", "manage.py", "runserver", "0.0.0.0:2137"]

