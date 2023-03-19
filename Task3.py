list_1 = [float(n) for n in input().split()]
list_2 = []
n = len(list_1)
n1 = 0
while n1 < n:
    a = int(abs(list_1[n1]))
    list_2.append(a)
    n1 += 1
print(*list_2)
