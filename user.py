class User:
  def __init__(self, name, email, password):
    self.id = 0 
    self.name = name
    self.email = email
    self.password = password
    
    self.reward_points = 0 
    self.bill_address = []
    self.mail_address = []
    self.preffered_diner = 0
    self.payment_method = ""

  def set_mail_address(self, m):
    self.mail_address = m 

  def set_bill_address(self, b):
    self.bill_address = b

  def add_points(self, points):
    self.points = self.points+points
  
  def set_id(self, id): 
    self.id = id 
  
  def get_id(self): 
    return self.id

  def get_info(self):
    return [self.id, self.name, self.password]

  def get_all_info(self):
    return [self.id, self.name, self.email,  self.password, self.mail_address[0], self.mail_address[1], self.mail_address[2], self.mail_address[3], self.bill_address[0], self.bill_address[1], self.bill_address[2], self.bill_address[3], self.reward_points, self.payment_method, self.preffered_diner]
  
  def add_credit_card(self, credit_card):
    self.credit_cards.append(credit_card)