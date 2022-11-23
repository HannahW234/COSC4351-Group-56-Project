from datetime import datetime
import holidays

print(datetime.today().isoweekday())


def is_weekend(date):
  try:
    date = datetime.strptime(str, '%Y-%m-%d').date()
    return date.isoweekday() == 7 or date.isoweekday() == 6
  except:
    return False


def is_holiday(date):
  return date in holidays.US()

