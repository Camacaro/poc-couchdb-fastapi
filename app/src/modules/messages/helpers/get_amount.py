from .is_digit_with_dot import is_digit_with_dot

def get_amount(s: str) -> str:
  first_item = s
  start_digits = False
  check = True
  amount = ""
  for item in first_item:
    if is_digit_with_dot(item) and check:
      start_digits = True
      amount += item
    elif start_digits:
      check = False
    
  return amount