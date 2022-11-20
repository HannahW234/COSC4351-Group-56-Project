import datetime


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
