line = list(map(float, input().split()))
total = 0
for i in line:
    total = total + i ** 2
print(total)