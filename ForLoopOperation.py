#simple for loop operation on list
colors = ['red','blue','green','yellow']
for x in colors:
    print(x)

#operation on String
S ='Python'
for c in S:
    print(c)

# Break the loop at 'blue'
colors = ['red','green','blue','yellow']
for color in colors:
    if color == 'blue':
        break
    print(color)

## Skip 'blue'
for color in colors:
    if color == 'blue':
        continue
    print(color)

#Else in for Loop
for color in colors:
    print(color)
else:
    print('done')

#range() function in for loop
for x in range(6):
    print(x)

## Increment the range with 2
for x in range(7,14,3):
    print(x)

# Flatten a nested list
list = [[1,2,3],[4,5,6],[7,8,9]]
for sublist in list:
    for number in sublist:
        print(number)

#Access Index in for Loop
colors = ['red','blue','green']
for index in range(len(colors)):
    print(index,colors[index])

#use the enumerate() function.
for index,value in enumerate(colors):
    print(index,value)

## Tuple unpacking
T =[(1,2),(3,4),(5,6)]
for (a,b) in T:
    print(a,b)

## Loop through two lists at once using zip()
name = ['Ajay','Vishal','Ravi']
age = [20,25,34]
for (a,b) in zip(name,age):
    print(a,b)