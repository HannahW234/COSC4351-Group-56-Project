class User:
  def __init__(self, name, email, password):
    self.id = 0 
    self.name = name
    self.email = email
    self.password = password
    self.phone_number = ''
    self.credit_cards = []

    self.reward_points = 0 
    self.bill_address = []
    self.mail_address = []
    self.preferred_diner = 0
    self.payment_method = ""

  def set_mail_address(self, m):
    self.mail_address = m 

  def set_bill_address(self, b):
    self.bill_address = b

  def add_points(self, points):
    self.reward_points += points
  
  def set_id(self, id): 
    self.id = id 
  
  def get_id(self): 
    return self.id

  def get_info(self):
    return [self.id, self.name, self.password]

  def get_all_info(self):
    return [self.id, self.name, self.email,  self.password, self.mail_address[0], self.mail_address[1], self.mail_address[2], self.mail_address[3], self.bill_address[0], self.bill_address[1], self.bill_address[2], self.bill_address[3], self.reward_points, self.payment_method, self.preferred_diner]
  
  def add_credit_card(self, credit_card):
    self.credit_cards.append(credit_card)
    
  def is_credit_card_on_file(self):
    return len(self.credit_cards) > 0
  
  def set_phone_number(self, phone_num):
    self.phone_number = phone_num
    
  def get_phone_number(self):
    return self.phone_number