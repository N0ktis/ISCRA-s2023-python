numbers = input().split()
res = list(map(float,numbers))
sum = 0
for number in res:
    sum += number ** 2
print(sum)

