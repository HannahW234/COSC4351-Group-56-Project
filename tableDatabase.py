import sqlite3
from table import Table
import functools


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
        new_table = Table(size, 2)
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
    data = c.fetchall()
    connection.commit()
    connection.close()
    return data


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


def find_tables(table_size):
    if table_size % 2 != 0:
        table_size += 1
    # reverse_data = fetchall()
    # reverse_data.reverse()
    result = []
    remaining = table_size

    if find_max_capacity() < table_size:
        return "Cannot create table"

    while remaining > 0:
        reverse_data = fetchall()
        reverse_data.reverse()
        for size, quantity in reverse_data:
            if quantity > 0 and remaining >= size:
                remaining -= size
                result.append(size)
                update_quantity(size)
                break
    return result


def find_max_capacity():
    return sum(list(map(lambda x: functools.reduce(lambda a, b: a * b, x), fetchall())))


delete_ALL()
create_table_information_database()
print(fetchall())
# update_quantity(8)
# print(fetchall())
# print(fetchall())
# print(find_tables(15))
# print(fetchall())