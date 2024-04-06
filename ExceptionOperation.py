'''Exceptions (Try…Except): When executing Python code, different errors may occur: coding errors made by the programmer,
 errors due to wrong input, or other unforeseeable things.
 If you don’t want this default behavior, you need to handle these exceptions.'''

#try and except Block: handle exception using try and except.
try:
    x = 1/0
except:
    print('something went wrong')
#something went wrong

#handle exception inside functions
def this_fails():
    x = 1/0
try:
    this_fails()
except Exception as e:
    print(e)
#devision by zero
    
#Catch Multiple Exceptions: You can define as many except blocks as you want, to catch and handle specific exceptions.
try:
    x = 1/0
except ZeroDivisionError:
    print('attampt to devide by zero')
except:
    print('something went wrong')

#If you want to execute the same block of code for multiple exceptions, specify all the exceptions in a parenthesized tuple.
try:
    x = 1/0
except (ZeroDivisionError,ValueError):
    print('zero devison error or else valeError')
except:
    print('something else went wrong')

#The Else Clause:(Optional) the else clause excute only when no exception raise.
try:
    x = 1/1
except:
    print('Something went wrong')
else:
    print('Nothing went wrong')
#Nothing went wrong

#The Finally Clause:(optional) It always execute wather exception raised or not, use for clean-up action
try:
    x = 1/0
except:
    print('something went wrong')
finally:
    print('always execute this')

#clean-up actions of finally.
'''f = open('setOperation.py')
try:
    print(f.read())
except:
    print('unable to find text file')
finally:
    f.close()
'''
#Raising an exception using 'raise'
#Raise built-in exception 'NameError'

raise NameError('an exception occure')
#raise NameError('an exception occure')

#User-defined Exceptions: You can create your own exceptions by creating a new exception class like this:
class inputErrorException(Exception):
    pass
raise inputErrorException('custom error')
#raise inputErrorException('custom error')
#__main__.inputErrorException: custom error



