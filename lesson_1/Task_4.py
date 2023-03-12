array = list(map(float, input().split()))
Sum = 0
for i in range(len(array)):
    Sum += array[i] * array[i]
print(Sum)