import string

# Helpers Functions
def remove_dot(s):
  str = s.replace(".", "")
  str = str.replace(",", "")
  return str

def is_digit_with_dot(s):
  for item in s:
    if item.isdigit() or item == "." or item == ",":
      return True
  return False

def remove_letters_lower_case(s):
  table = str.maketrans('', '', string.ascii_lowercase)
  return s.translate(table)

def remove_digits(s):
  str = ""
  for item in s:
    if not item.isdigit():
      str += item
  return str

def remove_sinpe_words(s):
  str = s.replace("BN SINPE MOVIL", "")
  str = str.replace("SINPE M", "")
  return str.strip()
# ================================================================

# Main Function
def get_referent(s):
  lastItem = s[-1]
  receipt = lastItem.split(" ")[-1]
  return remove_dot(receipt)

def get_amount(s):
  first_item = s[0]
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

def get_name(s):
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
# ================================================================

# Transacción validada correctamente
# {
#   "_id": "6020495e7f763500118ea0f6",
#   "name": "alexis gabriel gonzalez valenciano",
#   "phone": "+50684020062",
#   "comprobante": "2021010215283010127223427",
#   "amount": 15000,
#   "details": "pago"
#   "_V": 0
# }
# ================================================================
msg1 = "Ha recibido 5650 colones por BN SINPE MOVIL  de JESSICA CALVO CAMACHO.  FACTJUNJESSICAC. Referencia 2022070115283001010338436."
msg2 = "Ha recibido 35,000.00 Colones de RHONALD ALEJANDRO B por SINPE Movil, dolares. Comprobante 2022063015183010943161180."
msg3 = "Este es de una plataforma llamada Pei: Alonso te ha enviado 1.800,00 colones a tu cuenta CR * 7385 desde pei"

split1 = msg1.split(". ")
split2 = msg2.split(". ")

print(split1)
print(split2)

comprobante = get_referent(split1)
comprobante2 = get_referent(split2)
# print("comprobante:", comprobante)
# print("comprobante2:", comprobante2)

amount = get_amount(split1)
amount2 = get_amount(split2)
# print("amount:", amount)
# print("amount2:", amount2)

name = get_name(split1)
name2 = get_name(split2)
# print("name:", name)
# print("name2:", name2)

transaction = {
  "comprobante": comprobante,
  "amount": amount,
  "name": name
}

transaction2 = {
  "comprobante": comprobante2,
  "amount": amount2,
  "name": name2
}

print(transaction)
print(transaction2)