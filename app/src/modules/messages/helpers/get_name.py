from typing import List
from .remove_letters_lower_case import remove_letters_lower_case
from .remove_digits import remove_digits
from .remove_sinpe_words import remove_sinpe_words
from .remove_dot import remove_dot

def get_name(s: List[str]) -> str:
  first_item = s[0]
  str = remove_letters_lower_case(first_item)
  str = remove_digits(str)
  str = remove_sinpe_words(str)
  str = remove_dot(str)
  splitStr = str.split("  ")
  name = ""

  for item in range(1, len(splitStr)+1):
    aux = splitStr[-item]
    if aux != "":
      name = aux
      break

  return name.strip()