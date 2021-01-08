# docker_python

## Docker File Format
1. Take a Base Image 
2. Configure Working Directory
3. COPY the project
4. Install requirment
5. Mount volume to save data
6. Run application

## Example Dockerfile


      FROM python:3.8-slim
      WORKDIR /app
      COPY xpfarm-dashboard .
      RUN pip install -r requirements.txt
      EXPOSE 8000
      CMD ["/app/manage.py", "runserver", "0.0.0.0:8000"]


### If the port is occupied , exit the docker container and start again
