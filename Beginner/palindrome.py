import re

def is_palindrome(s):
    normalized = re.sub(r'[^a-zA-z0-9]','',s.lower())

    return normalized == normalized[::-1]

while True:
    text = input('Enter your text here: ')

    if is_palindrome(text):
        print(f'{text} is palindrome')
    else:
        print(f'{text} is not palindrome')

    user_input = input('Do you want to continue (yes/no): ' ).lower()

    if user_input == 'no':
        break
    elif user_input == 'yes':
        print('program will continue')
    else:
        print('invalid input')





