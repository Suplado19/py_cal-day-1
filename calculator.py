#Calculator program first version day 1

print('Welcome to the calculator program')

print('1. addition')
print('2. subtraction')
print('3. multiplication')
print('4. division')

choice =int(input('Enter choice between 1 to 4: '))

if choice == 1:
    num1 = float(input('enter first number:'))
    num2 = float(input('enter second number:'))
    result = num1 + num2
    print('The result of addition is:', result)
elif choice == 2:
    num1 = float(input('enter first number:'))
    num2 = float(input('enter second number:'))
    result = num1 - num2
    print('The result of subtraction is:', result)
elif choice == 3:
    num1 = float(input('enter first number:'))
    num2 = float(input('enter second number:'))
    result = num1 * num2
    print('The result of multiplication is:', result)
elif choice == 4:
    num1 = float(input('enter first number:'))
    num2 = float(input('enter second number:'))
    if num2 != 0:
        result = num1 / num2
        print('The result of division is:', result)
    else:
        print('Error: Division by zero is not allowed.')
else:
    print('Invalid choice. Please select a valid option.')