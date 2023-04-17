num = int(input('Please enter a number '))
def reverse(num):
    if num<10:
        return num
    else:
        return int(str(num%10)+str(reverse(num//10)))
if num==reverse(num):
    print('Palindrome')
else:
    print('Not Palindrome')