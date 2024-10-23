# Brenden Reed

def encode(password):
    result = ''
    for i in password:
        result += str(int(i)+3)[-1]
    return result
