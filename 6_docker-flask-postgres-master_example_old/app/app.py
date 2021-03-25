import time
from flask import Flask, render_template, flash, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}:{}@{}:{}/{}'.format('name','pass','db','5432','testdb')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'pass'
db = SQLAlchemy(app)

class students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    def __init__(self, name ): self.name = name

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if not request.form['name']: flash('Please enter all the fields', 'error')
        else:
            student = students(request.form['name'])
            db.session.add(student)
            db.session.commit()
    return render_template('show_all.html', students=students.query.all())


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0')
