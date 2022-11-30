import sqlite3
from user import User


def create_user_information_database():
  connection = sqlite3.connect('customer.db')
  
  c = connection.cursor()
  #creating table, dont run again becasue table has already been created
  c.execute("""CREATE TABLE IF NOT EXISTS customers (
          customer_id int, 
          name text,
          email text,
          password text, 
          mail_city text, 
          mail_state text, 
          mail_zip text, 
          mail_address text, 
          bill_city text, 
          bill_state text, 
          bill_zip text, 
          bill_address text, 
          points int, 
          payment_method text, 
          preferred_diner int
  )
  """)

  connection.commit()
  connection.close()

create_user_information_database()

def get_new_id(): #Genereates a unique ID for the new customer
  connection = sqlite3.connect('customer.db')
  
  c = connection.cursor()
  c.execute("SELECT * FROM customers")
  items = c.fetchall()
  connection.commit()
  connection.close()

  if len(items) == 0: #if table is empty and no codes 
    return 1000 
  else: 
    ids = [i[0] for i in items]
    return max(ids) + 1


def add_user(user: User):
  connection = sqlite3.connect('customer.db')
  
  c = connection.cursor()
  #to add to table
  id = 0 
  if not is_user_exist(user):
    id = get_new_id()
    user.set_id(id)
    print(user.get_all_info())
    c.execute("INSERT INTO customers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", user.get_all_info())
  
  connection.commit()
  connection.close()
  return id 

def delete_ALL():
  connection = sqlite3.connect('customer.db')
  
  c = connection.cursor()
  # to add to table
  c.execute("DELETE from customers")
  
  connection.commit()
  connection.close()

def fetchall():
  connection = sqlite3.connect('customer.db')
  
  c = connection.cursor()
  #to print from customers table
  c.execute("SELECT * FROM customers")
  print(c.fetchall())
  
  connection.commit()
  connection.close()
  
def get_id(user:User): 
  connection = sqlite3.connect('customer.db')
  
  c = connection.cursor()
  c.execute("SELECT customer_id, name, password FROM customers")
  user_info = user.get_info()
  items = c.fetchall()
  connection.commit()
  connection.close()
  for item in items: 
    if user_info[1] == item[1] and user_info[2] == item[2]: #comparing name and password 
      return item[0]

def get_address(id, type): 
  connection = sqlite3.connect('customer.db')
  
  c = connection.cursor()
  if type == "mail": 
    c.execute("SELECT customer_id, mail_zip, mail_city, mail_state, mail_address FROM customers WHERE customer_id = '%s'" % id)
  elif type == "bill":
    c.execute("SELECT customer_id, bill_zip, bill_city, bill_state, bill_address FROM customers WHERE customer_id = '%s'" % id)

  items = c.fetchall()
  items = items[0]
  connection.commit()
  connection.close()
  return items[1] + " " + items[2] + " " + items[3] + " " + items[4]
#
def is_user_exist(user: User) -> bool:
  connection = sqlite3.connect('customer.db')
  
  c = connection.cursor()
  c.execute("SELECT customer_id, name, password FROM customers")
  items = c.fetchall()
  
  found = False
  for item in items:
    if item == tuple(user.get_info()):
      found = True
      break

  connection.commit()
  connection.close()
  
  return found

def add_points(userID, points): 
  connection = sqlite3.connect('customer.db')
  
  c = connection.cursor()
  c.execute("SELECT customer_id, points FROM customers WHERE customer_id = '%s'" % userID)

  items = c.fetchall()
  new_points = items[0][1] + points
  c.execute("UPDATE customers SET points = ? WHERE customer_id = ?", (new_points, userID))

  connection.commit()
  connection.close()

def add_payment_method(userID, method):
  connection = sqlite3.connect('customer.db')
  
  c = connection.cursor()
  c.execute("UPDATE customers SET payment_method = ? WHERE customer_id = ?", (method, userID))

  connection.commit()
  connection.close()

def get_payment_method(userID): 
  connection = sqlite3.connect('customer.db')
  
  c = connection.cursor()
  c.execute("SELECT customer_id, payment_method FROM customers WHERE customer_id = '%s'" % userID)
  items = c.fetchall()
  method = items[0][1]

  connection.commit()
  connection.close()
  return method

def get_points(userID): 
  connection = sqlite3.connect('customer.db')
  
  c = connection.cursor()
  c.execute("SELECT customer_id, points FROM customers WHERE customer_id = '%s'" % userID)
  items = c.fetchall()
  points = items[0][1]

  connection.commit()
  connection.close()
  return points 

