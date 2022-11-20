from flask import Flask, render_template, session, request
from user import User
from userDatabase import *
from creditDatabase import * 
import tableDatabase as t 

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
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
  currentUserID = get_id(user)
  user.set_id(currentUserID)
  session['user'] = user.__dict__ ##allows for user to be used in other requests
  if is_user_exist(user): 
    session['logged_in'] = True
  
  return render_template("userloggedin.html", user_exist=is_user_exist(user))


@app.route('/registration', methods=["GET"])
def registration_page():
  return render_template("registration.html")

@app.route('/reservation', methods=["POST", "GET"])
def reservation_page():
  return render_template("reservation.html")

@app.route('/enter_payment', methods=["POST","GET"])
def enter_payment():
  name = request.form['credit_name']
  credit_num = request.form['credit_num']
  security = request.form['security_num']
  exp_date = request.form['expiration_date']
  
  if session['logged_in']: 
    currentUserID = session['user']['id']
    credit_info = [currentUserID, name, credit_num, security, exp_date]
    add_credit_card(credit_info)

  return render_template("paymentConfirmation.html")

@app.route('/payment', methods=["POST","GET"])
def payment_page():
  return render_template("payment.html")

@app.route('/newuser', methods=["POST", "GET"])
def creating_new_user_page():
  name = request.form['name']
  email = request.form['email']
  password = request.form['password']
  
  user = User(name, email, password)
  currentUserID = add_user(user)
  user.set_id(currentUserID)
  session['user'] = user.__dict__
  session['logged_in'] = True
  
  
  return render_template("userloggedin.html", user_exist=is_user_exist(user))

@app.route('/logout', methods=['GET'])
def logout():
  session['logged_in'] = False
  return render_template("index.html")

@app.route('/table', methods=["POST"])
def show_available_tables():
  time = request.form['time']
  date = request.form['date']
  size = request.form['size']
  
  t.delete_ALL()
  t.create_table_information_database()
  print(t.fetchall())

  # print(type(date))
  # print(type(time[0:2]))
  # print(type(size))
  table = t.Table(date, int(time[0:2]), int(size), None)
  result = t.find_tables(table)

  print(result)

  print(t.fetchall())


  return (f"{time[0:2]}")

if __name__ == "__main__":
  session.clear()
  app.run(debug=True)