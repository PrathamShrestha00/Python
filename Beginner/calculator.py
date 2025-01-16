def calculator():

    print('Welcome to simple calculator.')
    print('Operations: + = Addition, - = Substraction, * = Multiplication, / = Division')

    while True:
        try:
            num1 = float(input('Enter first number: '))
            op = input('Enter operation you want to perform: ').strip()
            num2 = float(input('Enter second number: '))

            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                result = num1 / num2
            else:
                print('Number cannot be divided by 0')

            print(f'The result is {result}')

        except ValueError:
            print('Invalid input')


        choice = input('Do you want to continue? (yes/no)').strip().lower()

        if choice != 'yes':
            print("closing app")
            break


calculator()
