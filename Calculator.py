def addition(number1, number2):
    return number1 + number2

def substract(number1, number2):
    return number1 - number2

def multiplication(number1, number2):
    return number1 * number2

def division(number1, number2):
    return number1 / number2

def modules(number1, number2):
    return number1 % number2

print('Please select Operations')
print('enter 1 for addition')
print('enter 2 for substraction')
print('enter 3 for multiplication')
print('enter 4 for devision')
print('enter 5 for modules')
flag=1
while(flag==1):
    operation = int(input('please enter Operation number(1 to 5)\n'))

    num1 = float(input("Enter first value\n"))
    num2 = float(input("Enter second value\n"))

    result = 0

    if operation == 1 :
        result = addition(num1, num2)
    elif operation == 2:
        result = substract(num1, num2)
    elif operation == 3:
        result = multiplication(num1, num2)
    elif operation == 4:
        result = division(num1, num2)
    elif operation == 5:
        result = modules(num1, num2)
    else:
        print('invalid operation')
    print(result)
    print("If you want to exit please enter '0' else '1'")
    flag = int(input())