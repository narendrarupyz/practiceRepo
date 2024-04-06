#Python’s Built-in csv library makes it easy to read, write, and process data from and to CSV files.
#/home/narendra-rupyz/test.csv
#open a csv file
f = open(r'/home/narendra-rupyz/test.csv')

#Specify File Mode: 'r': read, 'w' : write, 'a' : append, 'r+' : read and write, 'x' : 'create' (default read mode)
#open write mode
f = open('/home/narendra-rupyz/test.csv','w')
#to close csv file use 'close()'
f.close()

#append mode
f = open('/home/narendra-rupyz/test.csv','a')
f.close()

#read and write mode
f = open('/home/narendra-rupyz/test.csv','r+')
f.close()

#create mode
#f = open('/home/narendra-rupyz/test2.csv','x')
#f.close()

# check closed status use 'closed()' approach1SS
#f.closed()
#True

#approach 2 to check closed status using 'with' keyword
with open('/home/narendra-rupyz/test2.csv') as f:
    print(f.read())

#Read a CSV File:  using its reader() method. The reader() method 
#splits each row on a specified delimiter and returns the list of strings.
import csv
with open('/home/narendra-rupyz/test.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

#Write to a CSV File: use a writer object and its writerow() method to pass the data as a list of strings.
import csv
with open('/home/narendra-rupyz/test2.csv') as f:
    writer = csv.writer(f)
    writer.writerow(['Bob','26','Manager'])
    writer.writerow(['Michel','30','SalesMan'])

#Read a CSV File Into a Dictionary: using DictReader() method.
#The first row of the CSV file is assumed to contain the column names, which are used as keys for the dictionary.
import csv
with open('/home/narendra-rupyz/test.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

#If the CSV file doesn’t have column names like the file below, you should specify 
#your own keys by setting the optional parameter fieldnames.
import csv
with open('/home/narendra-rupyz/test.csv') as f:
    keys =['name','age','job']
    reader = csv.DictReader(f, fieldnames = keys)
    for row in reader:
        print(row)

#Write a CSV File From a Dictionary: using the DictWriter() method. Here it is necessary to specify the fieldname parameter.
import csv
with open('/home/narendra-rupyz/test3.csv') as f:
    keys = ['name','age','job','city']
    writer = csv.DictWriter(f, fieldnames = keys)
    writer.writeheader
    writer.writerow({'job':'Manger','age':'29','name':'Andrew','city':'London'})
    writer.writerow({'job':'Business Analysist','age':'26','name':'Rachit','city':'Delhi'})

#Use a different delimiter: The comma , is not the only delimiter used in the CSV files. You can use any delimiter of your choice such 
#as the pipe |, tab \t, colon : or semi-colon ; etc. using 'delimiter'
import csv
with open('/home/narendra-rupyz/test4.csv') as f:
    writer = csv.writer(f, delimiter = '|')
    writer.writerow({'job':'Tester','age':'35','Name':'Ravi','city':'Kolkata'})

#test.csv
#Ravi|35|Tester|Kolkata

#read this file, specifying the same delimiter.
import csv
with open('/home/narendra-rupyz/test4.csv') as f:
    reader = csv.reader(f, delimiter = '|')
    for row in reader:
        print(row)

#Handle Comma Within a Data
import csv
with open('/home/narendra-rupyz/test5.csv'):
    writer = csv.writer(f, quotechar = '"')
    writer.writerow({'Sam','24','developer','New York'})

#Catching and Reporting Errors
import csv, sys
fileName ='/home/narendra-rupyz/test4.csv'
with open(fileName, newline = '') as f:
    reader = csv.reader(f)
    try:
        for row in reader:
            print(row)
    except csv.Error as e:
        sys.exit('file {}','line {}:{}'.format(fileName, reader.line_num,e))