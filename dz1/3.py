print('введите строку чисел')
line = input()
res = list(int(abs(float(num))) for num in line.split())
for num in res:
    print(num, end=" ")
