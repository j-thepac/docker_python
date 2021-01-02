from flask import Flask, request
app = Flask(__name__)
@app.route('/')
def hello_world() -> str: return "Hello world"
if __name__ == '__main__':app.run(debug=True, host='0.0.0.0' ,port = 8000)


"""
Create a new folder
Copy Current file into the folder
Install docker
start docker
docker run -it --name myflask1 -p 5000:5000 -v ${PWD}:/app python:3.7 bash 
# logins to docker in interactive mode
#-p :  set port in local to docker port
#-v :  share the folder path inside docker

exit() #exit python shell and open Terminal
pip install flask
cd /app/
python flask_example_deepak.py
open 

"""