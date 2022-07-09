
def remove_sinpe_words(s):
  str = s.replace("BN SINPE MOVIL", "")
  str = str.replace("SINPE M", "")
  return str.strip()