from flask import Flask, render_template, session, request
from user import User
from userDatabase import *
from creditDatabase import * 
import tableDatabase as t
from datatype_check import *


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
create_user_information_database()

@app.route("/")
def home():
  t.create_table_information_database()
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

@app.route('/profile', methods=["POST", "GET"])
def profile_page(): 
  currentID = session['user']['id']
  credit_info = get_user_credit_data(currentID)
  #points = get_points(currentID)
  #favorite_diner = get_diner(currentID) ###NEED TO IMPLEMENT DINER SYSTEM
  #current_reservations = get_user_reservations(currentID) ##IMPLEMENT USER RESERVATIONS 
  name = session['user']['name']
  email = session['user']['email']
  mail_address = get_address(currentID, "mail")
  bill_address = get_address(currentID, "bill")
  profile_data = [name, email, credit_info, mail_address, bill_address]

  return render_template("profile.html", data=profile_data)

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
    session['points'] = 1

  return render_template("paymentConfirmation.html")

@app.route('/payment', methods=["POST","GET"])
def payment_page():
  return render_template("payment.html")

@app.route('/newuser', methods=["POST", "GET"])
def creating_new_user_page():
  name = request.form['name']
  email = request.form['email']
  password = request.form['password']

  mail_address = [request.form['m_city'], request.form['m_state'], request.form['m_zipcode'], request.form['m_street']]
  if not request.form['sameAsMailing']: 
    bill_address = [ request.form['b_city'], request.form['b_state'], request.form['b_zipcode'], request.form['b_street']]
  else: 
    bill_address = mail_address

  user = User(name, email, password)
  user.set_mail_address(mail_address)
  user.set_bill_address(bill_address)
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

  if not is_valid_date(date) and not is_valid_time(time):
    return render_template("reservation.html")


  hours, minutes = map(int, time.split(':'))

  client_table = t.Table(date, int(hours), int(size), None)
  t.fetchall()
  result = t.find_tables(client_table) #either will be empty list [] or list with tables that were reserved ie. [4,2,2]

  valid_table = is_table_reserved(result) #will check if it is empty or not, meaning table reserved or not
  user_test = User("random", "example@email.com","123456")
  display_info = display(user_test, client_table, t.find_tables)
  
  return render_template("tables.html", tables_reserved=result, table_info=client_table, valid_table=valid_table, display_info=display_info)

if __name__ == "__main__":
  app.run(debug=True)