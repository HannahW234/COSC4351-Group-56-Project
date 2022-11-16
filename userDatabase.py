import sqlite3
from user import User


def create_user_information_database():
  connection = sqlite3.connect('customer.db')
  
  c = connection.cursor()
  #creating table, dont run again becasue table has already been created
  c.execute("""CREATE TABLE IF NOT EXISTS customers (
          name text,
          email text,
          password text
  )
  """)

  connection.commit()
  connection.close()

  
def add_user(user: User):
  connection = sqlite3.connect('customer.db')
  
  c = connection.cursor()
  #to add to table
  if not is_user_exist(user):
    c.execute("INSERT INTO customers VALUES (?, ?, ?)", user.get_info())
  
  connection.commit()
  connection.close()


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
  

#
def is_user_exist(user: User) -> bool:
  connection = sqlite3.connect('customer.db')
  
  c = connection.cursor()
  c.execute("SELECT * FROM customers")
  items = c.fetchall()
  
  found = False
  for item in items:
    if item == tuple(user.get_info()):
      found = True
      break

  connection.commit()
  connection.close()
  
  return found

# user = User('hiris', 'example@domain.com', '123456')
# add_user(user)
#fetchall()

