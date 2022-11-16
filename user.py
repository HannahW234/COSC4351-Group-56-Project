class User:
  def __init__(self, name, email, password):
    self.name = name
    self.email = email
    self.password = password
    
    
  def get_info(self):
    return [self.name, self.email, self.password]