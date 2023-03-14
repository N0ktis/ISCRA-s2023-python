a = input()
sh = int(input())
b = ""
a = a.replace(" ", "")
for i in a:
    b+=chr(((ord(i)+sh)//123)*97+((ord(i)+sh)%123))
print(b)