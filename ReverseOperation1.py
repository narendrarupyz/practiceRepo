numberToReverse = 78346
reversed_number = 0
count = 0

while(numberToReverse > 0):
    mod = numberToReverse % 10
    print(mod)
    reversed_number = reversed_number * 10 + mod
    print(reversed_number)
    numberToReverse //= 10
    print(numberToReverse)
    count += 1
    print('count',count)
    

print(reversed_number)