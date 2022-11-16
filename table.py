class Table:
  def __init__(self, size, quantity):
    self.size = size
    self.quantity = quantity
    
  def get_info(self):
    return [self.size, self.quantity]
    