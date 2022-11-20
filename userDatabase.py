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
          password text 
  )
  """)

  connection.commit()
  connection.close()

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
    c.execute("INSERT INTO customers VALUES (?, ?, ?, ?)", user.get_info())
  
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
  for item in items: 
    if user_info[1] == item[1] and user_info[3] == item[2]: 
      return item[0]

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

