
import string

def remove_letters_lower_case(s):
  table = str.maketrans('', '', string.ascii_lowercase)
  return s.translate(table)