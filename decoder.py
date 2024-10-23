def decode(password2):
  decoded = ""
  for digit in password2:
    decoded += str(int(digit)-3)[-1]
  return decoded
