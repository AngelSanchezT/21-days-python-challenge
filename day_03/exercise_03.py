def is_leap_year(year):

  # not decimals years and negative
  if type(year) != int or year < 0:
    return False

  # Es divisible por 4, pero no por 100
  if (year % 4 == 0) and not(year % 100 == 0): 
    return True
  
  # Si es divisible por 100 debe serlo por 400 también
  if (year % 100 == 0) and (year % 400 == 0):
    return True

  return False

print(is_leap_year(2000)) # True
print(is_leap_year(-2024)) # False
print(is_leap_year(1984.25)) # False
