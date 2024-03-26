numberToReverse = 78346
reversed_number = 0

while(numberToReverse > 0):
    mod = numberToReverse % 10
    reversed_number = int(reversed_number * 10 + mod)
    numberToReverse = int(numberToReverse / 10)

print(reversed_number)