a = str(input())
a = a.split(" ")
sum = 0
for i in a:
    buffer = float(i)
    buffer = buffer*buffer
    sum = sum + buffer
print(sum)
