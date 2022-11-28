import sqlite3
from user import User
from datetime import datetime 

def create_reservation_info_database():
  connection = sqlite3.connect('reservations.db')
  
  c = connection.cursor()
  #creating table, dont run again becasue table has already been created
  c.execute("""CREATE TABLE IF NOT EXISTS reservation (
          customer_id int, 
          diner text,
          date date, 
          time time, 
          amount_people int,
          amount_spent int
  )
  """)

  connection.commit()
  connection.close()

create_reservation_info_database()

def add_reservation(reservation_data):
    #userID, diner, date, time, num_people, amount_spent, points
    connection = sqlite3.connect('reservations.db')
    c = connection.cursor()
    #to add to table
   
    c.execute("INSERT INTO reservation VALUES (?, ?, ?, ?, ?, ?)", reservation_data)
    
    connection.commit()
    connection.close()

def calculate_preffered_diner(userID): 
    connection = sqlite3.connect('reservations.db')
    c = connection.cursor()
    ## get all diners for user 
    c.execute("SELECT customer_id, diner FROM reservation WHERE customer_id = '%s'" % userID)
    items = c.fetchall()
    items = [i[1] for i in items]
    preffered_diner =  max(set(items), key=items.count)

    connection.commit()
    connection.close() 

    return preffered_diner

def get_user_reservations(userID):
    connection = sqlite3.connect('reservations.db')
    c = connection.cursor()
    ## get all diners for user 
    c.execute("SELECT * FROM reservation WHERE customer_id = '%s'" % userID)
    items = c.fetchall()
    items = [i[1:] for i in items]

    previous = [i for i in items if datetime.combine(datetime.strptime(i[1], '%Y-%m-%d').date(),  datetime.strptime(i[2], '%H:%M').time()) < datetime.now()]
    current = [i for i in items if datetime.combine(datetime.strptime(i[1], '%Y-%m-%d').date(),  datetime.strptime(i[2], '%H:%M').time())  >= datetime.now()] 

    connection.commit()
    connection.close() 

    return previous, current

