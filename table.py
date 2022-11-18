class Table:
  def __init__(self, date, time, size, quantity):
    self.date = date
    self.time = time
    self.size = size
    self.quantity = quantity
    
  def get_info(self):
    return [self.date, self.time, self.size, self.quantity]
    