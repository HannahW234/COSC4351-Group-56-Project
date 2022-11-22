class User:
  def __init__(self, name, email, password):
    self.id = 0 
    self.name = name
    self.email = email
    self.password = password
    self.reward_points = 0 

  def add_points(self, points):
    self.points = self.points+points
  
  def set_id(self, id): 
    self.id = id 
  
  def get_id(self): 
    return self.id

  def get_info(self):
    return [self.id, self.name, self.email, self.password]