#creation of Tuple
T = (1,2,3)

T
#(1,2,3)

#A Tuple of String
T = ('red','blue','green')
#('red','blue','green')

#Tuple of mixed data type
T = ('red',3,1.7,True)

T
#('red',3,1.7,True)

#Tuple without () parenthisis
T = 'red',3,1.7,True
T
#'red',3,1.7,True

#Single Tuple indicate this by including a trailing comma , just before the closing parentheses.
T = (5,)
T
#(5)

#Converting list to tuple
T = tuple([4,5,6])
T
#(4,5,6)

#Converting String to a tuple
T = tuple('red')
T
#('r','e','d')

#Nested Tuple
T = ('red','blue',('green','yellow'),'brown')
T
#('red','blue',('green','yellow'),'brown')
# Common errors in tuple unpacking

T = ('red', 'green', 'blue', 'cyan')
#(a, b) = T
# Triggers ValueError: too many values to unpack

#Tuple unpacking comes handy when you want to swap values of two variables without using a temporary variable.
a=78
b=55
a,b =b,a
a#55
b#78

#we can split string based on a value using split() method and tuple unpacking
addr = 'narendra@gmail.com'
a,b =addr.split('@')
a
#narendra
b
#gmail.com

#access Tuple value by indexing
T = ('red','blue','green')
T[0]#red
T[1]#blue
T[2]#green

#Negative indexes count backward from the end of the tuple.
T[-1]
#green

#Tuple Slicing it is smilar to list slicing
T = ('a','b','c','d','e')
T[::-1]
#('e','d','c','b','a')

#Change Tuple Items: simply it return error 
T = ('red', 'green', 'blue')
#T[0] = 'black'
# Triggers TypeError: 'tuple' object does not support item assignment

#Delete a Tuple: you can't delete items in tuple but can be completely delete by using del keyword
del T

#Tuple Concatenation & Repetition by using + and * opreator
T =(1,2,'red')+(5,6,7)
T
#(1,2,'red',5,6,7)

#Replecation
T =('red') * 3
T
#('red','red','red')

#Find Tuple length using len()
len(T)
#3

#Check item is available or not
T = ('red','blue','green')
if 'blue' in T:
    print('Yes')
if 'yellow' not in T:
    print('No')

#To iterate over the items of a tuple, use a simple for loop
for item in T:
    print(item)
'''
red
blue
green'''

#Tuple sorting method 1 by using tuple(sorted())
tuple(sorted(T))
#('blue','green','red')

#2nd method of sorting
T = ('green','blue','yellow')
temp = list(T)
temp.sort()
T = tuple(temp)
#('blue','green','yellow')
