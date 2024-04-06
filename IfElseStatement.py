X,Y =9,7

#if statement body only print when the statment is true
if X > Y :
    print("X is greater then Y")

# any non-zero value always return True
if -3:
    print(True)

#Nested if statement code block to begin a new code block
X,Y,Z = 8,6,3
if(X>Y):
    print('X is greater than Y')
    if(Y>Z):
        print('Y is greater than Z')

#The else Statement 'if condition not satisfy then else block will excute
if(X<Y):
    print('X is smaller than Y')
else:
    print('X is greater than Y')


#The elif (else if) Statement
x,y =6,6
if x > y:
    print('x is greater ')
elif y > x:
    print('y is greater ')
else:
    print('x and y are equal')

#Substitute for Switch Case
choice =5
if choice ==1:
    print('case 1')
elif choice ==2:
    print('case 2')
elif choice ==3:
    print('case 3')
elif choice ==4:
    print('case 4')
else:
    print('default case')

#Multiple Conditions
#if both condition true execute if block by using 'and'
x,y,z = 7,5,2
if x>y and x>Z:
    print('x is greater')
x,y,z = 7,6,8
#if either 1st or 2nd condition satisfied execute if block by using 'or'
if x>y or x>z:
    print('x is grater than y or z')

#not expression is True, if the condition is false.
if not x<y:
    print('x is not less than y')

#One Line if Statement
if x > y : print('x is greater than y')

#multi line statement, simply by separating them with a semicolon ';' .
x,y =7,5
if x > y : print('x is greater than y');print('x and y are not equal');print('y is not greater than x')

#Conditional Expressions (ternary operator)
x,y =5,7
print('x is greater than y')if x > y else print('y is greater than x')
