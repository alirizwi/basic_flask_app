from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/hello/<user>')
def hello_name(user):
   return render_template('layout.html', name = user)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

@app.route("/addUser", methods=["POST"])
def userAdd():
    user=request.form['username']
    email= request.form['email']
    db.create_all()
    new_person=User(user, email)
    db.session.add(new_person)
    db.session.commit()
    temp ={}
    temp['status']=(type(new_person)==User)
    return jsonify(temp)

@app.route("/users")
def userFetch():
    db.create_all()
    allUsers=User.query.all()
    strf = ''
    for user in allUsers:
        strf += user.username + "\n"
    return strf

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)