#To define a Python function, use def keyword. 
def hello():
    print("hello function")

hello()

 #Pass single argument to a function
def hello(name):
    print('hello',name)

hello('narendra')

# Pass two arguments
def employeeDetails(name,empid):
    print(F'Employee name : {name} employeeId :{empid}')
employeeDetails('Ravi',2036)

#Positional Arguments: values are copied to their corresponding parameters in order.
def func(name, job):
    print(name,' is a software',job)
func('Narendra','developer')

#Keyword Arguments : To avoid positional argument confusion.
#Keyword arguments can be put in any order
def func(name, job):
    print(job, name)
func(name='johany', job = 'Postman')

#Default Arguments: Set default value 'developer' to a 'job' parameter
def func1(name, job ='developer'):
    print(name,' is a ',job)
func1('Ravi')

#Variable Length Arguments (*args): 
#when you want to create functions that take unlimited number of arguments.
def multi_Args(*args):
    print(args)
multi_Args(3,54,3,65,7,32)

#**kwargs : The ** syntax is similar, but it only works for keyword arguments.
def key_argument(**kwargs):
    print(kwargs)
key_argument(name='Raushan', age="25", job='Salesman')

#Return Value : To return a value from a function, simply use a return statement.
def sum(a,b):
    return a+b
total_value =sum(34,89)
print(total_value)

#Return Multiple Values : Python has the ability to return multiple values.
# Return addition and subtraction in a tuple
def sum_sub(a,b):
    return a+b, a-b
multi_val = sum_sub(35,27)
print(multi_val)

# Unpack returned tuple
def func(a,b):
    return a+b, a-b
add, sub =func(66,35)
print(add, sub)

#Docstring: Docstrings are usually triple quoted to allow for multi-line descriptions.
def func():
    '''this function use
    to print multi line'''
    print('docString')
#help(func)
#print(hello.__doc__)

#Composition :One of the most useful features of Python is its ability to take small 
#building blocks and compose them.
import math
x =math.exp(math.log(3.14))
print(x)

#Nested Functions : A Nested function is a function defined within other function. 
def outer(a,b):
    def inner(c,d):
        return c+d
    return inner(a,b)
result =outer(34,87)
print(result)

#Recursion: A recursive function is a function that calls itself 
#and repeats its behavior until some condition is met to return a result.
def countdown(num):
    if num <= 0:
        print('stop')
    else:
        print(num)
        countdown(num-1)
countdown(8)

#Assigning Functions to Variables
def hello():
    print('hello')
hi=hello
hi()

#Python Function Executes at Runtime
x = 0
if x:
    def hello():
        print('hello world')
else:
    def hello():
        print('hello universe')
hello()



