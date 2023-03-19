string = input()
hop = int(input())
string = string.split()
array = list(string)
array = ''.join(str(i) for i in array)
newarray = []
for i in array:
    buffer = ((ord(i) - 97 + hop) % 25) + 97
    newletter = chr(buffer)
    newarray.append(newletter)
newarray = ''.join(str(i) for i in newarray)
print(newarray)

