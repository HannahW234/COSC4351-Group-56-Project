from flask import Flask, render_template, request
from user import User
from userDatabase import *
import tableDatabase as t
from datatype_check import *


app = Flask(__name__)
create_user_information_database()

@app.route("/")
def home():
  return render_template("index.html")

@app.route('/login', methods=["POST", "GET"])
def login_page():
  return render_template('login.html')

@app.route('/confirmation', methods=["POST", "GET"])
def confirmation_page():
  name = request.form['name']
  email = request.form['email']
  password = request.form['password']
  user = User(name, email, password)
  
  return render_template("userloggedin.html", user_exist=is_user_exist(user))
  


@app.route('/registration', methods=["GET"])
def registration_page():
  return render_template("registration.html")

@app.route('/reservation', methods=["POST", "GET"])
def reservation_page():
  return render_template("reservation.html")

@app.route('/payment', methods=["POST"])
def payment_page():
  return render_template("payment.html")

@app.route('/newuser', methods=["POST", "GET"])
def creating_new_user_page():
  name = request.form['name']
  email = request.form['email']
  password = request.form['password']
  
  user = User(name, email, password)
  add_user(user)
  
  return render_template("userloggedin.html", user_exist=is_user_exist(user))


@app.route('/table', methods=["POST"])
def show_available_tables():
  time = request.form['time']
  date = request.form['date']
  size = request.form['size']

  if not is_valid_date(date) and not is_valid_time(time):
    return render_template("reservation.html")

  t.delete_ALL()
  t.create_table_information_database()
  print(t.fetchall())
  hours, minutes = map(int, "00:00".split(':'))

  table = t.Table(date, hours, int(size), None)
  result = t.find_tables(table)

  print(result)

  print(t.fetchall())
  hours, minutes = map(int, "00:00".split(':'))
  return time

if __name__ == "__main__":
  app.run(debug=True)