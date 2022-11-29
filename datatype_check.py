import datetime
import re

from table import Table
from dateService import is_weekend, is_holiday


def is_valid_date(date):
    try:
        new_date = datetime.datetime.strptime(date, '%Y-%m-%d')
        if new_date < datetime.datetime.strptime(str(datetime.date.today()), '%Y-%m-%d'):
            return False
    except ValueError:
        return False

    return True

def is_valid_name(name):
    first_last_name_regex = re.compile(r"^([a-zA-Z]{2,}\s[a-zA-Z]{1,}'?-?[a-zA-Z]{2,}\s?([a-zA-Z]{1,})?)")
    
    if first_last_name_regex.match(name) == None:
        return False
    
    return True

def is_valid_time(date, time):
    try:
        new_time = datetime.datetime.strptime(time, '%H:%M').time()
        new_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        if new_date == datetime.date.today():
            if new_time < datetime.datetime.now().time():
                return False
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
        display_str.append(f"Diner Location: {table.getDiner()}")
        display_str.append(f"Name of reservation: {user_dict['name']}")
        display_str.append(f"Time of reservation: {datetime.datetime.strptime(str(table.time) + ':00','%H:%M').strftime('%I:%M %p')}")
        display_str.append(f"Date of reservation: {table.date}")
        display_str.append(f"Table for {table.size} is including: ")

        for table in reserving_tables:
            display_str.append(f"One Table for: {table} people")
    else:
        display_str.append("Could Not Reserve Table")
        
    return display_str
