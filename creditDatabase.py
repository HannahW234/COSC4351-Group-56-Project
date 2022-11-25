import sqlite3
from user import User

def create_credit_information_database():
  connection = sqlite3.connect('credit.db')
  
  c = connection.cursor()
  c.execute("""CREATE TABLE IF NOT EXISTS credit (
          customer_id int, 
          name text, 
          credit_num text,  
          security_num text,
          exp_date date
  )
  """)

  connection.commit()
  connection.close()

def add_credit_card(credit_info):
    connection = sqlite3.connect('credit.db')
  
    c = connection.cursor()
    #to add to table
    c.execute("INSERT INTO credit VALUES (?, ?, ?, ?, ?)", credit_info)
        
    connection.commit()
    connection.close() 

def get_user_credit_data(userID):
  connection = sqlite3.connect('credit.db')
  c = connection.cursor()
  print(userID)
  c.execute("SELECT * FROM credit WHERE customer_id = '%s'" % userID)
  items = c.fetchall()
  items = [i[1:] for i in items]

  connection.commit()
  connection.close() 

  return items

create_credit_information_database()

