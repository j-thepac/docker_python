from flask import request,Flask,json,render_template,jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///person.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}:{}@{}:{}/{}'.format('name','pass','db','5432','testdb')
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)

class Person(db.Model):
  id = db.Column('student_id', db.Integer, primary_key = True)
  fname = db.Column(db.String(100))
  def __init__(self, fname):  self.fname = fname

@app.route('/',methods = ['GET','POST'])
def index():
  if request.method=="GET":return render_template('input.html')
  elif  request.method=="POST":
      fname=request.form['fname']
      db.session.add(Person(fname))
      db.session.commit()
      return render_template("output.html", persons=Person.query.all())

@app.route("/<string:resource>/", methods = ['GET','POST'])
def api_hello(resource):
   if (resource == "deepak"):return "deepak"
   elif ('name' in request.args ):return (request.args['name'])
   elif( request.method == 'POST'):
     if request.headers['Content-Type'] == 'application/json':
       return json.dumps(request.json)
     else:return str(request.data)

@app.errorhandler(500)
def not_found(error=None):
   resp = jsonify({"message": 'not found'}) #dict to  json
   resp.status_code = 500
   return resp
   
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, host='0.0.0.0')
