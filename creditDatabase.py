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


create_credit_information_database()

