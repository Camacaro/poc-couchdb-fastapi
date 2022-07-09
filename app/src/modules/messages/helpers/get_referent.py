
from .remove_dot import remove_dot

def get_referent(s: str) -> str:
  lastItem = s[-1]
  receipt = lastItem.split(" ")[-1]
  return remove_dot(receipt)