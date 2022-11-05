import sqlite3

connection = sqlite3.connect('customer.db')

c = connection.cursor()

#creating table, dont run again becasue table has already been created
# c.execute("""CREATE TABLE customers (
#         first_name text,
#         last_name text,
#         email text,
#         phone_number integer,
#         mailing_address text,
#         billing_address text,
#         earned_points integer,
#         prefered_payment text
# )
#
# """)


#to add to table
#c.execute("INSERT INTO customers VALUES ('Fake', 'Customer', 'fakecustomer@gmail.com', '1234567890', '123 city blvd', '123 city blvd', '100', 'Cash')")

#to print from customers table
#c.execute("SELECT * FROM customers")
#print(c.fetchall())

#

connection.commit()

connection.close()