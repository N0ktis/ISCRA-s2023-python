from math import floor
li = input().split()
for i in range(len(li)):
    li[i] = floor(abs(float(li[i])))
print(*li)