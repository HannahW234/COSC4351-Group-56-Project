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
    #return type(data) == list
    return not data == []


def display(user_dict, table: Table, tables_result) -> list:
    
    reserving_tables = tables_result
    display_str = []

    if reserving_tables:
        display_str.append(f"Name of reservation: {user_dict['name']}")
        display_str.append(f"Time of reservation: {datetime.datetime.strptime(str(table.time) + ':00','%H:%M').strftime('%I:%M %p')}")
        display_str.append(f"Date of reservation: {table.date}")
        display_str.append(f"Table for {table.size} is including: ")

        for table in reserving_tables:
            display_str.append(f"One Table for: {table} people")
    else:
        display_str.append("Could Not Reserve Table")
        
    return display_str
