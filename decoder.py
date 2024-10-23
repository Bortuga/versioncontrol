def decode(password):
  decoded = ""
  for digit in password:
    decoded += str(int(digit)-3)[-1]
  return decoded