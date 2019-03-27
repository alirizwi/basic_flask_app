from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

@app.route('/hello/<user>')
def hello_name(user):
   return render_template('layout.html', name = user)

if __name__ == "__main__":
    app.run(debug=True)