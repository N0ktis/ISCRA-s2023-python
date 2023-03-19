a = str(input())
a = a.split(' ')
newarray = []
for i in a:
    buffer = int(abs(float(i))//1)
    newarray.append(buffer)
newarray = ' '.join(str(i) for i in newarray)
print(newarray)


