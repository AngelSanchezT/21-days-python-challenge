def calculate_tip(bill_amount, tip_percentage):
  tip_value = (bill_amount * tip_percentage) / 100
  return round(tip_value, 2)

print(calculate_tip(100, 10))
print(calculate_tip(1524.33, 25))
