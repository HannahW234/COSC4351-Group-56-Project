from datetime import datetime
import holidays


def is_weekend(date):
  try:
    date = datetime.strptime(date, '%Y-%m-%d').date()
    return date.isoweekday() == 7 or date.isoweekday() == 6
  except:
    return False


def is_holiday(date):
  return date in holidays.US()

