import math 

class Category:
  # Constructor
  def __init__(self, category):
    # Instance Variable
    self.category = category
    self.ledger = []

      
  # Deposit Method
  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})
    
  # Withdraw Method
  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -1 * amount, "description": description})
      return True
    else: 
      return False
      
  # Get_balance Method
  def get_balance(self):
    balance = 0.0
    for item in self.ledger:
      balance += item['amount']
    return balance
  
  # Transfer Method 
  def transfer(self, amount, budget_category):
    if self.withdraw(amount, "Transfer to " + budget_category.category):
      budget_category.deposit(amount, "Transfer from " + self.category)
      return True
    return False
  
  # Check_funds Method
  def check_funds(self, amount):
    if self.get_balance() >= amount:
      return True
    return False
    
  # Display
  def __str__(self):
    string = self.category.center(30,"*") + "\n" # Title ('***Food***')
    for item in self.ledger:
      # Limit description to the first 23 character [:23] and right align to the space provided (:23). Left align the amount to the space provided (:7) and make the amount two decimal places (2f)
      line = f"{item['description'][:23]:<23}{item['amount']:>7.2f}"
      string += line + "\n"
    string += "Total: " + str(self.get_balance())
    return string

def create_spend_chart(categories):

  spends = []

  # Get spends in each category 
  for category in categories: 
    spend = 0 
    for item in category.ledger:
      if item['amount'] < 0:
        spend += abs(item['amount'])
    spends.append(spend)

  # Calculate Percentage spent by category. Round down to the nearest 10.
  totalSpend = sum(spends)
  percentages = [i/totalSpend * 100 for i in spends]
  
  title = "Percentage spent by category\n"
  chart = ""

  # Range(100, -1, -10) -> create a sequence of numbers from 100 to 0, but decrement by 10. Right align the numbers.
  for i in range(100, -1, -10):
    # Create the y axis
    chart += str(i).rjust(3) + "|" 
    # Create the bars 
    for percent in percentages:
      if percent > i:
        chart += " o "
      else:
        chart += "   "
    # There's one extra column ("-") at the end. Need to fill that with " "
    chart += " \n"
    
  # Add the lines for the x axis
  # Add spaces as part of the x axis. So the lines are indented.
  x_axis = "    " + "-" * (3 * len(categories) +1) + "\n"
  
  # Categories
  category_list = []
  category_length = []

  for category in categories:
    category_list.append(category.category)
    category_length.append(len(category.category))
    
  max_length = max(category_length)

  # Left align (take up the space of the longest category). If not done, labels will cut to the shorted category. 
  category_list = list(map(lambda category: category.ljust(max_length), category_list))

  # For vertical labels
  for category in zip(*category_list):
    x_axis += "    " + "".join(map(lambda s: s.center(3), category)) + " \n"

  answer = (title + chart + x_axis).rstrip("\n")

  print(answer)

  return answer
  

  
        
      
      
  