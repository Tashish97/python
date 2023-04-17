num = int(input('Please enter a number: '))
a,b,i=0,1,0
while i<num:
    print(a)
    temp = a+b
    a = b
    b = temp
    i+=1
