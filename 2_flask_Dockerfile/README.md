#Run Using Dockerfile

- cd to folder containing DockerFile
- run command 

        docker build -t any_name:0.1 .  
        docker images #to check the images
        docker run -it --rm -p 5000:5000  2_flask:latest
    


## gunicorn :
- installs app server
- uwsgi can also be used


Use API tool like - Jmeter or Postman etc ., 
http://0.0.0.0:5000 

    Module defines following APIs:
        GET     '/'         - returns greetings string
        POST    '/cadbury'  - add cadbury            
        GET     '/cadbury   - checks if cadbury is present
        DELETE  '/cadbury   - deletes cadbury
        


##Can be run manually as well by:
 - Manually creating a python image and bind maping the current folder 
    
        docker run -it --name myflask1 -p 8000:8000 -v ${PWD}:/app python:3.7 bash 
    
- Manually installing requirement.txt
- Run below command
        
        gunicorn --bind=0.0.0.0:8000 --workers=1 chocolates:app

