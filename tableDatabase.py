import datetime
import sqlite3
from table import Table
import functools


def isDateAlreadyInDatabase(date):
    connection = sqlite3.connect('tables.db')
    c = connection.cursor()
    
    quanitityQuery = ("SELECT * FROM remainingTables WHERE reservation_date == ?")
    c.execute(quanitityQuery, (date,))
    item = c.fetchall()
    
    connection.commit()
    connection.close()

    return len(item) > 0


def create_table_information_database():
    connection = sqlite3.connect('tables.db')

    c = connection.cursor()
    # creating table, dont run again becasue table has already been created
    c.execute("""CREATE TABLE IF NOT EXISTS remainingTables (
          reservation_date DATE,
          reservation_time INTEGER,
          tablesize INTEGER ,
          quantity INTEGER
  )
  """)
    days_in_advance = 2
    base = datetime.datetime.today()
    date_list = [(base - datetime.timedelta(days=-x)).date() for x in range(days_in_advance)]
    for date in date_list:
        # if the day already exist in database, then dont create new tables on that day
        if isDateAlreadyInDatabase(date):
            continue
        for time in range(12, 15, 2):
            for size in range(2, 5, 2):
                #date.strftime('%Y-%m-%d')
                new_table = Table(date, time, size, 2)
                add_table(new_table)
        

    connection.commit()
    connection.close()


def add_table(table: Table):
    connection = sqlite3.connect('tables.db')

    c = connection.cursor()
    # to add to table
    c.execute("INSERT INTO remainingTables VALUES (?, ?, ?, ?)", table.get_info())

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
    data = c.fetchall()
    connection.commit()
    connection.close()
    return data


def update_quantity(table: Table):
    connection = sqlite3.connect('tables.db')
    c = connection.cursor()


    quanitityQuery = ("SELECT * FROM remainingTables WHERE reservation_date == ? AND reservation_time == ? AND "
        "tablesize == ?")
    c.execute(quanitityQuery, (table.date, table.time, table.size,))
    item = c.fetchone()
    if not item or item[3] < 1:
        connection.commit()
        connection.close()
        return False

    sqlquery = (f"UPDATE remainingTables SET quantity = {item[3] - 1} WHERE reservation_date == ? AND  reservation_time == ? AND "
                "tablesize == ?")
    c.execute(sqlquery, (table.date, table.time,table.size,))
    connection.commit()
    connection.close()

    return True


def find_tables(clientTable: Table):
    client_size = clientTable.size
    if clientTable.size % 2 != 0:
        client_size += 1

    result = []
    remainingClient = client_size

    connection = sqlite3.connect('tables.db')
    c = connection.cursor()

    quantityQuery = ("SELECT tablesize, quantity FROM remainingTables WHERE reservation_date == ? AND reservation_time == ?")
    c.execute(quantityQuery, (clientTable.date, clientTable.time,))
    item = c.fetchall()

    if find_max_capacity(item) < client_size:
        connection.commit()
        connection.close()
        return []

    while remainingClient > 0:
        c.execute(quantityQuery, (clientTable.date, clientTable.time,))
        availableTables = c.fetchall()
        availableTables.reverse()

        for tableSize, tableQuantity in availableTables:
            if tableQuantity > 0 and remainingClient >= tableSize:
                remainingClient -= tableSize
                result.append(tableSize)
                newTable = Table(clientTable.date, clientTable.time, tableSize, find_quantity(clientTable))
                update_quantity(newTable)
                break

    connection.commit()
    connection.close()
    return result


def find_quantity(table:Table):
    connection = sqlite3.connect('tables.db')
    c = connection.cursor()
    size = table.size
    if size % 2 == 1:
        size += 1
    quanitityQuery = ("SELECT quantity FROM remainingTables WHERE reservation_date == ? AND reservation_time == ? AND tablesize == ?")
    c.execute(quanitityQuery, (table.date, table.time, table.size,))
    quantity = c.fetchone()

    connection.commit()
    connection.close()

    return quantity


def find_max_capacity(sequence):
    return sum(list(map(lambda x: functools.reduce(lambda a, b: a * b, x), sequence)))

