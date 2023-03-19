list_1 = [float(n) for n in input().split()]
n = 0
while n < len(list_1):
    list_1[n] = list_1[n] ** 2
    n += 1
print(sum(list_1))
