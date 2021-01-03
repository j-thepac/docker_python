FROM python:3
WORKDIR /app
COPY django_dockerfile .
RUN pip install -r requirements.txt
VOLUME /data
RUN python manage.py collectstatic
CMD ["uwsgi", "django_dockerfile_uwsgi.ini"]



