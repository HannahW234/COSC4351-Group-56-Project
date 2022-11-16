from flask import Flask, render_template, request
from user import User
from userDatabase import *


app = Flask(__name__)
create_user_information_database()

@app.route("/")
def home():
  return render_template("index.html")

@app.route('/login', methods=["POST"])
def login_page():
  return render_template('login.html')

@app.route('/confirmation', methods=["POST"])
def confirmation_page():
  name = request.form['name']
  email = request.form['email']
  password = request.form['password']
  user = User(name, email, password)
  
  return render_template("userloggedin.html", user_exist=is_user_exist(user))
  


@app.route('/registration', methods=["GET"])
def registration_page():
  return render_template("registration.html")

@app.route('/reservation')
def reservation_page():
  return render_template("reservation.html")

@app.route('/newuser', methods=["POST"])
def creating_new_user_page():
  name = request.form['name']
  email = request.form['email']
  password = request.form['password']
  
  user = User(name, email, password)
  add_user(user)
  
  return render_template("userloggedin.html", user_exist=is_user_exist(user))


if __name__ == "__main__":
  app.run(debug=True)