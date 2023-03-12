line = input()
n = int(input())
line1 = ''

for x in line:
    if x == ' ':
        line1 += ' '
    elif x.islower():
        line1 += chr((ord(x) + n - 97) % 26 + 97)
    else:
        line1 += chr((ord(x) + n - 65) % 26 + 65)
print(line1)
