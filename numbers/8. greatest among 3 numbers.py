a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
c = int(input('Enter 3rd number: '))

if a>c and a>b:
    print("1st number is greatest")
elif b>a and b>c:
    print('2nd number is greatest')
else:
    print('3rd number is greatest')