# Brenden Reed

def encode(password1):
    result = ''
    for i in password1:
        result += str(int(i)+3)[-1]
    return result
