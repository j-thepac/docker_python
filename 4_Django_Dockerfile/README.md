
# Existing django project 


## Pre-Req (If ur creating ur own django project):
- install python 3+
- install docker 

        - pip install virtualenv
        - source ./bin/activate #
        - pip install -r requirments.txt
        - django-admin startproject django_dockerfile
        - python manage.py runserver
               
## Pre-Req (If you want to use the project from this repo):        
- make sure to add in settings.py 
- where 'data' folder is volumn mounted in below steps

        STATIC_ROOT = '/static'
        
        DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': '/data/db.sqlite3',
        }
        }


## Steps :
- build image
- mount persistant volume
- create DB and place it in persistant volumne somewhere inside a container
- Create SuperUser


        $ cd django_dockerfile #inside the project where u have docker file 
        $ docker build -t django_dockerfile .
        $ docker volume create django_dockerfile_db
        $ docker run -it --rm -v django_dockerfile_db:/data django_dockerfile python manage.py migrate 
        $ docker run -it --rm -v django_dockerfile_db:/data django_dockerfile python manage.py createsuperuser
        $ docker run -it --name django_dockerfile -p 8000:8000 -v django_dockerfile_db:/data django_dockerfile

## Explain Dockerfile 

- Take a Base Image 
- Configure Working Directory
- COPY the project
- Install requirment
- Mount volume to save data
- Run application and gather all static files into a folder called staticfiles in our project root directory
- After that run command "uwsgi django_dockerfile.ini"

        FROM python:3
        WORKDIR /app
        COPY django_dockerfile .
        RUN pip install -r requirements.txt
        VOLUME /data
        RUN python manage.py collectstatic
        CMD ["uwsgi", "django_dockerfile_uwsgi.ini"]

        
## uwsgi
Serves  static files 
        
      
## Manual
        
        $ docker run -it --rm --name django_dockerfile -p 8000:8000 -v ${PWD}:/app python:3 bash
