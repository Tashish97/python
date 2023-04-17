num = int(input('Enter a number: '))
rev,temp = 0,num
while num!=0:
    rev = rev*10 + num%10
    num = num//10
if rev ==temp:
    print("palindrome")
else:
    print("not palindrome")