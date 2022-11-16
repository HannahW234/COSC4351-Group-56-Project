import sqlite3
from table import Table


def create_table_information_database():
  connection = sqlite3.connect('tables.db')
  
  c = connection.cursor()
  # creating table, dont run again becasue table has already been created
  c.execute("""CREATE TABLE IF NOT EXISTS remainingTables (
          tablesize INTEGER ,
          quantity INTEGER
  )
  """)
  
  for size in range(2, 9, 2):
    new_table = Table(size, 1)
    add_table(new_table)
  
  connection.commit()
  connection.close()


def add_table(table: Table):
  connection = sqlite3.connect('tables.db')
  
  c = connection.cursor()
  # to add to table
  c.execute("INSERT INTO remainingTables VALUES (?, ?)", table.get_info())
  
  connection.commit()
  connection.close()


def delete_ALL():
  connection = sqlite3.connect('tables.db')
  
  c = connection.cursor()
  # to add to table
  c.execute("DELETE from remainingTables")
  
  connection.commit()
  connection.close()


def fetchall():
  connection = sqlite3.connect('tables.db')
  
  c = connection.cursor()
  # to print from remainingTables table
  c.execute("SELECT * FROM remainingTables")
  print(c.fetchall())
  
  connection.commit()
  connection.close()
  
def update_quantity(table_size):
  connection = sqlite3.connect('tables.db')
  
  c = connection.cursor()
  c.execute("SELECT * FROM remainingTables")
  items = c.fetchall()
  availability = False
  for item in items:
    if item[0] == table_size and item[1] > 0:
      c.execute(f"UPDATE remainingTables SET quantity = {item[1] - 1} "
                f"WHERE tablesize = {item[0]}")
      availability = True
      break
    
  connection.commit()
  connection.close()
  
  return availability
