from user import *
from creditCardServices import *
import random
from userDatabase import add_user, create_user_information_database
first_names =('John','Andy','Joe', 'Mary', 'Tracy', '')
last_names =('Johnson','Smith','Williams', 'Martinez', 'Perez')
DINERS = ["Pink's Pizza", "Buffalo Bayou Brewery", "Space City Diner", "Galveston Grill", "Midtown Deli"]

def create_sample_users(listOfDiners):
  SIZE = 10
  PASSWORD = "123456"
  NAMES = [random.choice(first_names) + " " + random.choice(last_names) for index in range(0, SIZE)]
  EMAILS = [f'{name.lower().replace(" ", "")}@email.com' for name in NAMES]
  address_sample = [
    "Example City",
    "EX",
    77000,
    ""
  ]
  customers = []
  for index in range(0, SIZE):
    new_user = User(NAMES[index], EMAILS[index], PASSWORD)
    new_user.set_id(random.randint(0, 100) + SIZE * random.randint(1, 10) - random.randint(0, 30))
    new_user.add_points(random.randint(0, 1000))
    new_user.set_phone_number(f"{str(index) * 10}")
    new_user.add_credit_card(create_credit_card_sample(NAMES[index], index))
    new_user.preferred_diner = random.choice(listOfDiners)
    new_user.payment_method = random.choice(("cash", "check", "credit"))
    address_sample[3] = f"{index * random.randint(1, 17) * 54} Sample Street"
    new_user.set_mail_address(address_sample)
    new_user.set_bill_address(address_sample)
    customers.append(new_user)
    
  return customers
  
  
def create_credit_card_sample(name, index):
    card_num = f"4551-0454-3859-302{index}"
    card_cvv = random.randint(100, 9999)
    card_exp_date = f'2025-0{random.randint(1, 9)}'
    
    return CreditCard(name, card_num, card_exp_date, card_cvv)

def create_users_sample_database():
 #ONLY RUN ONCE TO CREATE THE USER SAMPLE IN DATABASE
  users = create_sample_users(DINERS)
  create_user_information_database()
  for user in users:
    add_user(user)


create_users_sample_database()