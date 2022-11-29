import flask
from flask import Flask, render_template, session, request, redirect, url_for

from dateService import is_weekend, is_holiday
from user import User
from userDatabase import *
from creditDatabase import * 
import tableDatabase as t
from datatype_check import *
from creditCardServices import *
from reservationDatabase import *
import datetime as dt


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
create_user_information_database()
#session['logged_in'] = False

@app.route("/")
def start():
  session['logged_in'] = False
  session['user'] = None
  t.create_table_information_database()
  return render_template("index.html")

@app.route("/home", methods=["POST", "GET"]) ###Different URL so that user is not logged out
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
  card_on_file = True if len(session['user']['credit_cards']) > 0 else False
  session['card_on_file'] = card_on_file
  
  if is_user_exist(user): 
    session['logged_in'] = True
  
  return render_template("userloggedin.html", user_exist=is_user_exist(user))
  


@app.route('/registration', methods=["GET"])
def registration_page():
  return render_template("registration.html")

@app.route('/reservation', methods=["POST", "GET"])
def reservation_page():
  today = str(dt.date.today())
  one_month_advance = str(dt.date.today() + dt.timedelta(days=30))
  
  return render_template("reservation.html", date=today, one_month_advance=one_month_advance)

@app.route('/enter_payment', methods=["POST","GET"])
def enter_payment():
  name = request.form['credit_name']
  credit_num = request.form['credit_num']
  security = request.form['security_num']
  exp_date = request.form['expiration_date']

  time = request.form['client_time']
  size = request.form['client_size']
  date = request.form['client_date']
  diner = request.form['reservation_diner']
  
  user_credit_card = CreditCard(name, credit_num, exp_date, security)
  session['user']['credit_cards'].append(user_credit_card.__dict__)
  session['card_on_file'] = True
  
  if session['logged_in']: 
    currentUserID = session['user']['id']
    credit_info = [currentUserID, name, credit_num, security, exp_date]
    add_credit_card(credit_info)

  points = int(size)
  if is_weekend(date) or is_holiday(date): 
    points = points + 5 
  return render_template("paymentConfirmation.html", valid_credit=user_credit_card.is_card_valid(), client_date=date, client_time=time, client_size=size, reservation_diner=diner, points = points)

@app.route('/payment', methods=["POST","GET"])
def payment_page():
  return render_template("payment.html")

@app.route('/newuser', methods=["POST", "GET"])
def creating_new_user_page():
  name = request.form['name']
  email = request.form['email']
  password = request.form['password']
  phone_number = request.form['phone_number']
  mail_address = [request.form['m_city'], request.form['m_state'], request.form['m_zipcode'], request.form['m_street']]
  
  if not request.form['sameAsMailing']: 
    bill_address = [ request.form['b_city'], request.form['b_state'], request.form['b_zipcode'], request.form['b_street']]
  else: 
    bill_address = mail_address

  user = User(name, email, password)
  user.set_mail_address(mail_address)
  user.set_bill_address(bill_address)
  user.set_phone_number(phone_number)
  currentUserID = add_user(user)
  user.set_id(currentUserID)
  session['user'] = user.__dict__
  session['logged_in'] = True
  session['card_on_file'] = False

  return render_template("userloggedin.html", user_exist=is_user_exist(user))

@app.route('/logout', methods=['GET'])
def logout():
  session['logged_in'] = False
  session['user'] = {}
  return render_template("index.html")

@app.route('/profile', methods=["POST", "GET"])
def profile_page(): 
  currentID = session['user']['id']
  credit_info = get_user_credit_data(currentID)
  points = get_points(currentID)
  favorite_diner = calculate_preffered_diner(currentID) ###NEED TO IMPLEMENT DINER SYSTEM
  previous_reservations, current_reservations = get_user_reservations(currentID) ##IMPLEMENT USER RESERVATIONS 
  name = session['user']['name']
  email = session['user']['email']
  mail_address = get_address(currentID, "mail")
  bill_address = get_address(currentID, "bill")
  profile_data = [name, email, credit_info, mail_address, bill_address, favorite_diner, current_reservations, points]

  return render_template("profile.html", data=profile_data)

@app.route('/unregistered_user_input_info', methods=["GET", "POST"])
def unregistered_user_input_info():
  password = ''
  name = request.form['name']
  phone = request.form['phone_number']
  email = request.form['email']
  
  user = User(name, email, password)
  user.set_phone_number(phone)
  session['user'] = user.__dict__
  session['card_on_file'] = False
  
  
  return redirect(url_for('processing_data', date=session['date'], time=session['time'], size=session['size'], diner=session['diner']))

@app.route('/reservations', methods=['POST', 'GET'])
def reservations_page():
  currentID = session['user']['id']
  previous, current = get_user_reservations(currentID)
  return render_template("myReservations.html", current_reservations=current, previous_reservations = previous)

@app.route('/table', methods=["POST"])
def show_available_tables():
  time = request.form['time']
  date = request.form['date']
  size = request.form['size']
  diner = request.form['diner']
  session['time'] = time
  session['date'] = date
  session['size'] = size
  session['diner'] = diner


  if not is_valid_date(date) or not is_valid_time(date, time):
    return redirect(url_for('reservation_page'))

  if not session['logged_in']: #Unregistered guest
    return render_template("login_unregistered.html")

  return processing_data(session['date'], session['time'], session['size'], session['diner'])

@app.route('/processing_data/<date>/<time>/<size>/<diner>', methods=["POST", "GET"])
def processing_data(date, time, size, diner):
  is_high_traffic_day = is_weekend(date) or is_holiday(date)
  if (is_high_traffic_day and not session['logged_in']) and not session['card_on_file']: #Unregistered guest on holiday/weekend
    newTable = Table(date, time, size, 0)
    newTable.setDiner(diner)
    return render_template("payment.html", client_table=newTable)

  hours, minutes = map(int, time.split(':'))

  client_table = t.Table(date, int(hours), int(size), None)
  client_table.setDiner(diner)
  t.fetchall()
  result = t.find_tables(client_table)  # either will be empty list [] or list with tables that were reserved ie. [4,2,2]

  valid_table = is_table_reserved(result)  # will check if it is empty or not, meaning table reserved or not
  client = session['user'] ##this is currently not working, needs to be user object not dict
  display_info = display(client, client_table, result)
  

  ###Adding reservation to reservation table for usr data / profile 
  price = int(size) + 0.00
  if is_weekend(date) or is_holiday(date): 
    price = price + 5
  reservation_data = [session['user']['id'], diner, date, time, size, price]
  if valid_table:
    if session['logged_in']:
      add_reservation(reservation_data)
      add_points(session['user']['id'], int(price))
  
  
  return render_template("tables.html", tables_reserved=result, table_info=client_table, valid_table=valid_table, display_info=display_info, is_high_traffic_day=is_high_traffic_day)




if __name__ == "__main__":
  app.run(debug=True)
