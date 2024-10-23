# Brenden Reed

from encoder import encode
from decoder import decode

if __name__ == '__main__':
    password1 = ''
    password2= ''
    while True:
        print('\nMenu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')

        menu_option = input('Please enter an option: ')

        if menu_option == '1':
            password1 = input('Please enter your password to encode: ')
            print('Your password has been encoded and stored!')
        elif menu_option == '2':
            password2 = encode(password1)
            print(f'The encoded password is {encode(password1)}, and the original password is {decode(password2)}.')
        elif menu_option == '3':
            break

