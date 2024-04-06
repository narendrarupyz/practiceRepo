'''Nested Dictionary: A dictionary can contain another dictionary, which in turn can contain 
dictionaries themselves, and so on to arbitrary depth.
Nested dictionaries are one of many ways to represent 'structured information'/'''

#Create a Nested Dictionary:
D ={'emp1':{'name':'Sam','job':'Manager'},
    'emp2':{'name':'Bob','job':'Dev'},
    'emp3':{'name':'Tom','job':'CTO'}}
print(D)

#The dict() Constructor: There are several ways to create a nested dictionary using a type constructor called dict().
D =dict(emp1 = {'name':'Sam','job':'Manager'},
        emp2 = {'name':'Bob','job':'Dev'},
        emp3 = {'name':'Tom','job':'CTO'})
print(D)

#use dict() function along with the zip() function, to combine separate lists of keys and values obtained dynamically at runtime.
IDs = ['emp1','emp2','emp3']

empInfo = [{'name':'Sam','job':'Manager'},
          {'name':'Bob','job':'Dev'},
          {'name':'Tom','job':'CTO'}]
D = dict(zip(IDs,empInfo))
print(D)

#default values for each key. The fromkeys() method offers a way to do this.
IDs =['emp1','emp2','emp3']
Default = {'name':'','job':''}
D = dict.fromkeys(IDs,Default)
print(D)

#Access Nested Dictionary Items
D ={'emp1':{'name':'Sam','job':'Manager'},
    'emp2':{'name':'Bob','job':'Dev'},
    'emp3':{'name':'Tom','job':'CTO'}}
print(D['emp1']['name'])
#Sam
print(D['emp2']['job'])
#Dev

#To avoid KeyError use get() insted of [].
print(D['emp1'].get('job'))
#Manager
print(D['emp1'].get('city'))
#None

#Change Nested Dictionary Items
D['emp1']['name'] = 'Manmohan'
D['emp1']['job'] ='Sales Manager'
print(D['emp1']['name'])

#Add or Update Nested Dictionary Items
D ={'emp1':{'name':'Sam','job':'Manager'},
    'emp2':{'name':'Bob','job':'Dev'},
    'emp3':{'name':'Tom','job':'CTO'}}
D['emp2'] = {'name': 'Kim', 'job': 'Dev'}
print(D)

#Add
D['emp4'] = {'name':'Michel','job':'Security Guard'}
print((D))

#Merge Two Nested Dictionaries using 'update()'
D1 = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
      'emp2': {'name': 'Kim', 'job': 'Dev'}}

D2 = {'emp2': {'name': 'Sam', 'job': 'Dev'},
      'emp3': {'name': 'Max', 'job': 'Janitor'}}
D1.update(D2)
print(D1)

#Remove an Item by Key: using pop()
x = D1.popitem()
print(D1)
#{'emp1': {'name': 'Bob', 'job': 'Mgr'}, 'emp2': {'name': 'Sam', 'job': 'Dev'}}

#If you don’t need the removed value, use the del statement.
del D['emp2']

#Iterate Through a Nested Dictionary
D ={'emp1':{'name':'Sam','job':'dev'},
    'emp2':{'name':'Tom','job':'Tester'},
    'emp3':{'name':'Karan','job':'dev'}}
for ids, info in D.items():
    print('\nEmployee ID',ids)
    for key in info:
        print(key,' ',info[key])

#Comperhensive Dict.
D = {(k,v): k+v for k in range(2) for v in range(2)}
print(D)
#{(0, 0): 0, (0, 1): 1, (1, 0): 1, (1, 1): 2}