def sum_of_num(num):
    if num<10:
        return num
    else:
        return num%10+sum_of_num(num//10)

print(sum_of_num(123))