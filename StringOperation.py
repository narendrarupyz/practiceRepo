#String creation
s ='hellow word'

#Multiline String by unging """ """ or ''' '''
S = """String literal can span
    in multiple line"""

#The str() Constructor use to convert in equivilent String
S= str(42)
S

#String slicing capability provided by python
S ='ABCDEFGHI'
print(S[1:5])
#BCDE
print(S[5:-1])
#FGH
print(S[2:8:3])
#CF
print(S[:-1])
#ABCDEFGH
print(S[::-1])
#IHGFEDCBA
print(S[:-8:-3])
#IFC
#[start:end:step]
#CF

#Replace method using replace()
S = 'Hellow World'
x = S.replace('World','Universe')
print(x)

#Split and jion using split() and join()
S ='red,blue,green,yellow'
x = S.split(',')
print(x)
J =','.join(x)
print(J)

# 1st printf-style % string formatting
S = '%s is %d years old.' %('Bob',20)
print(S)

# 2nd format() Built-in Method
S = '{0} is {1} years old.'.format('Bob',25) 
print(S)

#3rd f-String Formatter
age = 30
name = 'Michel'
S =f"{name} is {age} years old"
print(S)

#Slicing a String S[start:stop:step]
S = '12345678'
print(S[1:6:2])
#for reverse
print(S[::-1])
print(S[7:2:-2])

#Slice with Positive & Negative Indices
print(S[2:-3:2])





