'''Python provides a wide range of built-in functions for file handling. It makes it really easy to create,
 update, read, and delete files.'''

#Open a File: using 'open('file location') with full path'
f =open(r'/home/narendra-rupyz/test.txt')

#it is assumed that the file is located in the same folder as Python. 
#f = open('test.txt')

#read entire file
print(f.read())
#from test text file

#we can specify the maximum number of characters to read.
print(f.read(5))

#Read Lines: default single line
print(f.readline())

#readlines(): if you want to read all line into list of String
print(f.readlines)
f.close()

#open a file for writing
#f = open('/home/narendra-rupyz/test.txt','w')

#open a file for reading and writing
f = open('/home/narendra-rupyz/test.txt','r+')
f.close()

#open a binary file for reading
f = open('/home/narendra-rupyz/test.txt','rb')
f.close()

f = open('/home/narendra-rupyz/test.txt','w')
#Write a File: Use the write() built-in method to write to an existing file, note file shold be open
print(f.write('overwrite existing data '))
f.close()

#Append mode ‘a’
f = open('/home/narendra-rupyz/test.txt','a')
print(f.write(' append this text.'))
f.close()

f = open('/home/narendra-rupyz/test.txt','r+')
f.write('----overwrite content----')
f.close()

#Write Multiple Lines
f = open('/home/narendra-rupyz/test.txt','w')
lines = ['new line1\n','new line2\n','new line3\n']
f.writelines(lines)
f.close()

f = open('/home/narendra-rupyz/test.txt','r')
print(f.read())
#new line1
#new line2
#new line3
f.close()

# Python recommends, as it automatically takes care of closing the file once it leaves the with block 
f = open('/home/narendra-rupyz/test.txt','r')
try:
    f.read()
finally:
    f.close()

#Create a New File: If you try to open a file for writing that does not exist, Python will automatically create the file for you.
f = open('test1.txt', 'w')
f.close
f = open('test2.txt','x')
f.close

#Delete a File: delete a file by importing the OS module and using its remove() method.
import os
os.remove('test1.txt')

#Check if File Exists
import os
if os.path.isfile('test2.txt'):
    f = open('test2.txt')
else:
    print('the file doesn\'t exit.'  )


