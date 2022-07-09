
def is_digit_with_dot(s):
  for item in s:
    if item.isdigit() or item == "." or item == ",":
      return True
  return False