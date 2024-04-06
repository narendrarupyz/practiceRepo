'''Variable Scope: The part of the program where the variable is accessible is called 
its “scope” and is determined by where the variable is declared.
-three different variable scopes:'''

#Local Scope: A variable declared within a function has a LOCAL SCOPE. 
#It is accessible from the point at which it is declared until the end of the function,
def myFunc():
    x=0
    print(x)
myFunc()

#Global Scope: A variable declared outside all functions has a GLOBAL SCOPE.
x = 45
def myFunc():
    print(x) #print 45

myFunc()
print(x) #print 45

#Modifying Globals Inside a Function
x = 45
def myFunc():
    x=0 
    print(x) # print x = 0

myFunc()
print(x) # print x = 45

x=50
def myFunc():
    global x
    x = 0
    print(x) #now it print 0

myFunc()
print(x) # here also print 0, because of 'global' keword it allow inside block to reassign value


#Enclosing Scope: If a variable is declared in an enclosing function, it is nonlocal to nested functions. 
#It allows you to assign to variables in an outer, but no-global, scope.
def myFunc1():
    x = 42
    def myFunc2():
        x = 0
        print(x) # x is 0
    myFunc2()
    print(x) # x is still 42
myFunc()

#nonlocal keyword: Preventing that behavior is where the nonlocal keyword comes in.
def myFunc1():
    x = 45
    def myFunc2():
        nonlocal x
        x = 0
        print(x) # print x = 0
    myFunc2()
    print(x) # print x = 0 because of 'nonlocal' keyword
myFunc()