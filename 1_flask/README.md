- Create a new folder
- Copy Current file into the folder
- Install docker
- start docker

        docker run -it --name myflask1 -p 5000:5000 -v ${PWD}:/app python:3.7 bash 
        
        # logins to docker in interactive mode
        #-p :  set port in local to docker port
        #-v :  share the folder path inside docker
    
        exit() #exit python shell into  Terminal
        pip install flask
        cd /app/
        python flask_example_deepak.py
        
open link  http://0.0.0.0:8000/ 