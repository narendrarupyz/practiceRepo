#simple while loop
x = 3
while x:
    print(x)
    x -=1

L =['red','blue','green']
while L:
    print(L.pop())

## Iterate until string is empty
L = 'blue'
while L:
    print(L)
    L =L[1:]

x = 6
while x:
    print(x)
    x -= 1
    if x==3:
        break

#Continue in while Loop
while x:
    x -=1
    if x % 2 !=0:
        continue
    print(x)

#Else in While Loop
x=5
while x:
    print(x)
    x -= 1
else:
    print('done')

#Infinte Loop (while true)
while True:
    name = input('enter your name : ')
    #print(name)
    if name == 'stop': break
    print(name)