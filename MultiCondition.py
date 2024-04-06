number_list =[]
for num in range(1,11):
    number_list.append(num)

print(number_list)

num_string = ','.join(str(v)for v in number_list)

print(num_string)

even_num = 0
odd_num = 0
for num in num_string:
    if num.isdigit():
        int_val = int(num)
        if int_val % 2 == 0:
            even_num += int_val
        else:
            odd_num += int_val

print(f"even numer sum is {even_num}, odd number sum is {odd_num}")

#reverse value mathematically
rev_String=''
new_String = ''.join(str(v) for v in number_list)
new_int = int(new_String)
while new_int > 0:
    rev = str(new_int % 10)
    new_int = int(new_int / 10)
    rev_String = rev_String + rev

print(rev_String)