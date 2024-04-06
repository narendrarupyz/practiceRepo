'''Dictionary: Dictionaries are Python’s implementation of a data structure, generally known as associative arrays, 
   hashes, or hashmaps.
   The association of a key and a value is called a key:value pair or sometimes an item.
'''
#Create a Dictionary: You can create a dictionary by placing a comma-separated list of key:value pairs in curly braces {}. 
D ={'name': 'Maxwell',
    'age' : 29,
    'job' : 'Professional Cricketer',
    'city': 'Sidney' }

D
#{'name': 'Maxwell', 'age': 29, 'job': 'Professional Cricketer', 'city': 'Sidney'}

'''The dict() Constructor: You can convert two-value sequences into a dictionary with Python’s dict() constructor. 
The first item in each sequence is used as the key and the second as the value.'''
#Create a dictionary with a list of two-item tuples
L = [('name','Michel'),
     ('job','dev'),
     ('age',30)]
D = dict(L)
D
#{'name': 'Michel', 'job': 'dev', 'age': 30}

# Create a dictionary with a tuple of two-item lists
T =(['name','Rachit'],
    ['job','UI developer'],
    ['age',28],
    ['city','Delhi'])
D = dict(T)
D
#{'name': 'Rachit', 'job': 'UI developer', 'age': 28, 'city': 'Delhi'}

#When the keys are simple strings, it is sometimes easier to specify key:value pairs using keyword arguments.
D = dict(name = 'Vishwajit',
         age =30,
         job = 'dev')
D
#{'name': 'Vishwajit', 'age': 30, 'job': 'dev'}

#use dict() function along with the zip() function, to combine separate lists of keys and values obtained dynamically at runtime.
Keys = ['name','job','age']
Values = ['Sam','Tester',30]
D = dict(zip(Keys,Values))
D
#{'name': 'Sam', 'job': 'Tester', 'age': 30}

# Initialize dictionary with default value '0' for each key, using fromkeys().
Keys = ['a','b','c']
defaultValue = 0
D = dict.fromkeys(Keys,defaultValue)
D
#{'a': 0, 'b': 0, 'c': 0}

#Keys must be unique:key more than once during the creation of a dictionary, the last value for that key becomes the associated value.
D = {'name':'Pravin','job':'Tech Support','age':30,'name':'Monu'}
#print(D)
#{'name': 'Monu', 'job': 'Tech Support', 'age': 30}

#Key must be immutable type:use any object of immutable type as dictionary keys – such as numbers, strings, booleans or tuples.
D = {(2,3):25,
    True:'a',
    'name':'Bob'}
#print(D)
#{(2, 3): 25, True: 'a', 'name': 'Bob'}

#Value can be of any type:
D = {'a':{1,3,4},
     'b':[3,4,6]}
#print(D)
#{'a': {1, 3, 4}, 'b': [3, 4, 6]}

#Access Dictionary Items: by passing keys in square bracket.
D = {'name':'Sam','age':26,'job':'dev'}
#print(D['name'])
#Sam
#print(D['Sal'])
#KeyError: 'Sal'

#get() method: This method never raise 'keyError' if key not in dict. return 'none'
print(D.get('name'))
#Sam
print(D.get('sal'))
#None

#Add or Update Dictionary Items: we can add and update using [],if key is new it will add in Dict.
D = {'name' : 'Raman','job':'Driver','city':'Hyderabad'}
D['name'] = 'Ravi'
#print(D['name'])
#Ravi
D['sal'] = 20000
#print(D['sal'])
#20000

#Merge Two Dictionaries: using 'update()' merge the keys and values of one Dict. into another
#Dict., this method blindly overwrites value of same key if there is a clash
D1 = {'name':'Sujeet','age':32,'city':'Mumbai'}
D2 = {'sal':67000,'email':'sujeet@web.com'}
D1.update(D2)
print(D1)
#{'name': 'Sujeet', 'age': 32, 'city': 'Mumbai', 'sal': 67000, 'email': 'sujeet@web.com'}

#Remove an item by key:
D = {'name':'Anand','age':30,'city':'Indore'}
x = D.pop('age')
print(x)
#30

#If you don’t need the removed value, use the del statement.
del D['city']
#print(D)

#Remove Last Inserted Item: popitem() method use to remove last inserted item and returned it.
D ={'name':'Vishwajeet','job':'UI dev','age':29}
x = D.popitem()
#print(x)
#('age', 29)

#Remove all Items: clear(), to delete all keys and value from dict, it return empty dict. 
D.clear()
print(D)
#{}

#Get All Keys, Values and Key:Value Pairs:there are 3 methods keys()'provides list of keys',
#values()'provides list of values' and items()'provides set of key:value', if you want in list wrap them in list().
D = {'name':'James','age':38,'job':'SalesMan'}
ListOfKeys = list(D.keys())
print(ListOfKeys)
#['name', 'age', 'job']
ListOfValues = list(D.values())
print(ListOfValues)
#['James', 38, 'SalesMan']
ListOfItems = list(D.items())
print(ListOfItems)
#[('name', 'James'), ('age', 38), ('job', 'SalesMan')]

#Iterate Through a Dictionary: If you use a dictionary in a for loop, it traverses the keys of the dictionary by default.
#iterate keys
for item in D:
    print(item)

#iterate values
for item in D:
    print(D[item])

#Check if a Key or Value Exists: use 'in' and 'not in' operator with 'if statement'
D = {'name':'James','age':38,'job':'SalesMan'}
print('name' in D)
#True
print('salary' in D)
#False
print('James' in D.values())
#True
print(30 in D.values())
#False

#Find Dictionary Length: using len(
print(len(D))
#3

