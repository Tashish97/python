num = int(input('Enter a number: '))
for i in range(2,num//2):
    if num%i==0:
        print('Number is not a prime number')
        break
else:
    print('Number is a prime number')
