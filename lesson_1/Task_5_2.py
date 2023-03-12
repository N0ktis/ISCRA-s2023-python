String = input()
CodeString = []
key = int(input())
for i in range(len(String)):
    num = ord(String[i]) + key
    CodeString.append(chr(num))
print(''.join(CodeString))