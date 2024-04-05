#Set{}: Python set is an unordered collection of unique items. 
#it is mutable, unique, unordered, unidexed
s ={'red','blue','green'}
print(s)
#{'blue', 'red', 'green'}

#Set constructor: You can also create a set using a type constructor called set().
S = set('abc')
print(S)
#{'b', 'a', 'c'}

#Add Items to a Set: You can add a single item to a set using 'add()' method.
s = {'red','blue','green'}
s.add('orange')
print(s)
#{'orange', 'blue', 'green', 'red'}

#You can add multiple items to a set using update() method.
s = {'red','blue'}
s.update(['yellow','pink'])
print(s)
#{'pink', 'red', 'blue', 'yellow'}

#Remove Items from a Set: remove a single item from a set, use 'remove()' or 'discard()' method.
s.remove('red')
print(s)
#{'yellow', 'pink', 'blue'}
s.discard('yellow')
print(s)
#{'blue','pink'}

#The pop() method removes random item from a set and returns it
s ={'red','blue','green'}
s.pop()
print(s)
#{'green','red'}

#clear(): Use clear() method to remove all items from the set.
s.clear()
print(s)
#set()

#len(): to find size of set
s = {'red','blue'}
x =len(s)
print(x)

#Iterate Through a Set: using for loop
s = {'pen','book','note book'}
for item in s:
    print(item)

#Check if Item Exists in a Set: using 'if' statement
colors ={'red','blue','green'}
if 'blue' in colors:
    print('yes')

if 'blue' not in colors:
    print('yes')
else:
    print('no')

#Set Operations: union() or | 
#You can perform union on two or more sets using union() method or  |  operator.
#to get all data from both variable
A ={'red','blue','green'}
B ={'yellow','red','orange'}

#by method
print(A.union(B))
#{'red', 'orange', 'green', 'blue', 'yellow'}

#by operator
print(A | B)
#{'red', 'orange', 'green', 'blue', 'yellow'}

#Set Intersection: intersection on two or more sets using 'intersection()' method or  '&'  operator.
#only matched data from both variable
#By method
print(A.intersection(B))
#{'red'}

#By opreator
print(A & B)
#{'red'}

#Set Difference: compute the difference between two or more sets using difference() method or  -  operator.
#Set Difference of A and B is the set of all items that are in A but not in B.
#By using method
A ={'red','blue','green'}
B ={'yellow','red','orange'}
print(A.difference(B))
#{'blue','green'}

#By operator
print(A - B)
#{'blue','green'}

#Set Symmetric Difference: compute symmetric difference between two or more sets using 
#'symmetric_difference()' method or  '^'  operator.
#return all data excepted matched data
A ={'red','blue','green'}
B ={'yellow','red','orange'}

#By method
print(A.symmetric_difference(B))
#{'blue', 'green', 'orange', 'yellow'}

#By operator
print(A ^ B)
#{'blue', 'green', 'orange', 'yellow'}

#Python Frozenset: (buit-in)Frozenset is just like set, only immutable (unchangeable).
#By frozenset()
s =frozenset({'red','blue','green'})
print(s)



