
"""
`check_fever` should return `True` if the temperature is `100.4` or higher. For
any lower temperature, it should return `False`.
"""
def check_fever(temperature):
  if temperature >= 100.4:
    return True
  
  else:
    return False

temp = float(input("What is my temperature?: \n"))
if check_fever(temp):
  print("You have a fever.")
else:
  print("You don't have a fever.")