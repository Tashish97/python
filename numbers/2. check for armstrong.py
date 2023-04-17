num = int(input('Enter the number: '))
temp = num
sum = 0
while num!=0:
    sum = sum+(num%10)**3
    num = num//10
if sum==temp:
    print('Number is an armstrong number')
else:
    print('Number is not an armstrong number')
