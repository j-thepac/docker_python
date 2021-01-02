# -*- coding: utf-8 -*-
"""
Use API tool like - Jmeter or Postman etc .,

    Module defines following APIs:
        GET     '/'         - returns greetings string
        POST    '/cadbury'  - add cadbury
        GET     '/cadbury   - checks if cadbury is present
        DELETE  '/cadbury   - deletes cadbury

"""

from flask import Flask, request

app = Flask(__name__)
chocos=[]

@app.route('/', methods=['GET'])
def list_chocolates() -> str:

    if len(chocos)>0:
        response = "<p>List of chocolates</p>"
        response += "<ul>"
        for choco in chocos:
            response += "<li>{}</li>".format(choco)
        response += "</ul>"
    else:
        response = "<p>No chocolates found. Please add with '/box/chocolate_name' POST request</p>"
    return response

@app.route('/<string:choco>', methods=['GET', 'POST', 'DELETE'])
def manage_chocolates(choco) -> str:
    if request.method == 'POST':
            chocos.append(choco)
            return "'{}' added.".format(choco)

    elif request.method == 'DELETE':
        if choco in chocos:
            chocos.remove(choco)
            return "{} removed".format(choco)
        else:
            return "{} Is not present in list of chocolates".format(choco)

    elif request.method == 'GET':
        if choco in chocos:
            return "{} is present".format(choco)
        else:
            return "{} is not present".format(choco)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8000)
