from datetime import datetime
import re

class CreditCard:
  def __init__(self, cardName, cardNum, expDate, CVV):
    self.cardName = str(cardName)
    self.cardNum = str(cardNum)
    self.expDate = expDate
    self.CVV = CVV
    
  
  def is_card_valid(self):
    first_last_name_regex = re.compile(r"^([a-zA-Z]{2,}\s[a-zA-Z]{1,}'?-?[a-zA-Z]{2,}\s?([a-zA-Z]{1,})?)")
    
    if first_last_name_regex.match(self.cardName) == None:
      return False

    if not self.is_card_num_valid():
      return False

    try: #checking expiration date is after today
      self.expDate = datetime.strptime(self.expDate, '%Y-%m-%d').date()
      if self.expDate < datetime.now().date():
        return False
    except:
      return False
    
    try: #CVV format and number
      self.CVV = int(self.CVV)
      if self.CVV < 100 or self.CVV > 9999:
        return False
    except:
      return False
  
    return True


  def is_card_num_valid(self):
    pattern1 = r"(\d{4})(-?)(\d{4})(\2\d{4}){2}"
    pattern2 = r"((\d)(?!\2{3})){16}"
    pattern3 = r'(?:\d{4}[ \-]?){3}\d{4}'
    return re.match(pattern3, self.cardNum) != None
  
  
credit = CreditCard("Hin Pham", "1111051051051010", '2022-12-01', 755)
print(credit.is_card_valid())
