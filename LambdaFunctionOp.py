'''Lambda Function: A lambda is simply a way to define a function in Python. known as lambda operators
 or lambda functions.'''

#Normal function
def doubler(x):
    return x * 2
print(doubler(5))
print(doubler(7))

#same function using lambda function.
#syntax lambda argument: expersion
doubler = lambda x : x * 2
print(doubler(8))

#No Statements Allowed: A lambda function can not contain any statements in its body.
'''eg  doubler = lambda x : assert x * 2
return, raise, pass, or assert in a lambda function will raise a SyntaxError. '''

#Single Expression Only: Unlike a normal function, a lambda function contains only a single expression.
evenOdd = (lambda x : 
'odd' if x % 2 else 'even')
print(evenOdd(13))
print(evenOdd(10))

#Immediately Invoked Function Expression (IIFE): passing args end of expression
print((lambda x : x*2)(5))

#Multiple Arguments: just seprate args by ','
mul = lambda a,b : a * b
print(mul(23,78))

#Ways to Pass Arguments: Like a normal function, a lambda function supports all the different 
#ways of passing arguments. This includes:

# Positional arguments
add = lambda x,y,z : x + y + z
print(add(23,43,67))
#133

# Keyword arguments
add = lambda x,y,z : x + y +z
print(add(45,y=23,z=34))
#102

# Default arguments
add = lambda x,y=20,z=12 : x + y + z
print(add(20))
#52

# *args
add  = lambda *args : sum(args)
print(add(3,5,8))
#16

# **args
add  = lambda **kwargs : sum(kwargs.values())
print(add(x=4,y=10,z=23))
#37

#Lambdas With Map, Filter, and Reduce: by using map(), filter(), and reduce().
#With map(): The map() function expects two arguments: a function and a list.

# Double each item of the list
def doubler(x):
    return x * 2
L = [1,2,3,4,5,6]
mod_list =map(doubler,L)
print(list(mod_list))
#[2, 4, 6, 8, 10, 12]

#Double each item of the list using lambda and map()
L=[1,2,3,4,5,6]
doubler = map(lambda x: x * 2, L)
print(list(doubler))
#[2, 4, 6, 8, 10, 12]

#With filter(): # Filter the values above 18 without lambda
def checkAge(age):
    if age > 18:
        return True
    else:
        return False
age = [23,12,45,67,14,17]
adults = filter(checkAge, age)
print(list(adults))
#[23, 45, 67]

#filter() with lambda
age = [23,12,45,67,14,17]
adults = filter(lambda x: x>18, age)
print(list(adults))
#[23, 45, 67]

'''With reduce(): It applies a rolling calculation to all items in a list. 
You can use it to calculate the total sum or to multiply all the numbers together.
'''
#sum all items in a list using reduce() function without a lambda.
from functools import reduce
def summer(a, b):
    return a+b
L =[23,43,65,7,89,7]
result = reduce(summer,L)
print(result)
#234

#by using reduce() with lambda
from functools import reduce
summer = reduce(lambda a,b: a+b, L)
print(summer)
#234

#Return Multiple Values
#Return multiple values by packing them in a tuple
findSquareCube = lambda num: (num**2,num**3)
square, cube = findSquareCube(2)
print(F'square is {square} and cube is {cube}')
#square is 4 and cube is 8

#if else in a Lambda
# A lambda function that returns the smallest item
findMin = lambda x, y : x if x<y else y
print(findMin(5,9))

#List Comprehension in a Lambda
# Flatten a nested list with lambda
flatten = lambda l : [item for sublist in l for item in sublist]
L =[[1,2,3],[4,5,6],[7,8,9]]
print(flatten(L))

'''Lambda Key Functions: key functions are higher-order functions that take another function 
(which can be a lambda function) as a key argument
 sorted(), min(), max() and List method: sort()'''

# Sort the list of taples by the age of students
L = [('Ram',45),('Rocky',23),('Anurabh',34)]
x =sorted(L, key=lambda student:student[0])
print(x)

#Lambda Closures: 
multiplier = (lambda x: (lambda y: x*y))

doubler = multiplier(2)
print(doubler(10))
# Prints 20

tripler = multiplier(3)
print(tripler(10))
# Prints 30




