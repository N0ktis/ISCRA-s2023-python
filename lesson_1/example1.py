a = (input())
a = a.split(' ')
sum = 0
newarray = []
for i in a:
    buffer = (float(i))
    newarray.append(buffer)
    sum = sum + buffer
print(sum)
