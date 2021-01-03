# docker_python

## Docker File Format
1. Take a Base Image 
2. Configure Working Directory
3. COPY the project
4. Install requirment
5. Mount volume to save data
6. Run application

## Example Dockerfile


    FROM python:3
    WORKDIR /app
    COPY bookmarks .
    RUN pip install -r requirements.txt
    VOLUME /data
    RUN python manage.py collectstatic
    CMD ["uwsgi", "bookmarks_uwsgi.ini"]


### If the port is occupied , exit the docker container and start again
