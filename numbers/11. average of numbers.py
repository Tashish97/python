size = int(input('Enter the size of array: '))
array=[]
for i in range(size):
    print(f"Enter element at index {i} ",end="")
    array.append(int(input()))
avg = sum(array)/size
print(f'Average of the given inputs are {avg}')