num = int(input('Enter a number:  '))
rev = 0

def reverse_recursion(num):
    '''
    A function to reverse a number with recursion
    '''
    if num<10:
        return num
    else:
        return int(str(num%10) + str(reverse_recursion(num//10)))
rec = reverse_recursion(num)
print("With Recursion: ",rec)

# solving recursion with iteration
while num!=0:
    rev = rev*10 + num%10
    num = num//10
print("With Iteration: ",rev)