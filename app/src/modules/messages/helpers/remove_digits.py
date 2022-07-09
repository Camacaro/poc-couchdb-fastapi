
def remove_digits(s):
  str = ""
  for item in s:
    if not item.isdigit():
      str += item
  return str