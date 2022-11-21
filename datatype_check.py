import datetime

import tableDatabase
from table import Table
from user import User


def is_valid_date(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return False

    return True

def is_valid_time(time):
    try:
        datetime.datetime.strptime(time, '%H:%M')
    except ValueError:
        return False

    return True


def is_table_reserved(data):
    return type(data) == list


def display(user: User, table: Table, find_table_func) -> list:
    user_info = user.get_info()
    table_info = table.get_info()
    
    reserving_tables = find_table_func(table)
    display_str = []

    if reserving_tables:
        display_str.append(f"Name of reservation: {user.name}")
        display_str.append(f"Time of reservation: {table.time}")
        display_str.append(f"Date of reservation: {table.date}")
        display_str.append(f"Table for {table.size} is including: ")

        for table in reserving_tables:
            display_str.append(f"One Table for: {table} people")
    else:
        display_str.append("Could Not Reserve Table")
        
    return display_str
