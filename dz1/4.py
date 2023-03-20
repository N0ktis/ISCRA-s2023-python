import math

print('введите строку чисел')
line = input()
result = sum(math.pow(float(num), 2) for num in line.split())
print(result)
