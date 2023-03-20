String = input()
CodeString = []
key = int(input())
key = key % 26
for i in range(len(String)):
    Ch = String[i]
    if Ch.isupper():
        CodeString.append(chr((ord(Ch) + key - 64) % 26 + 65))
    else:
        CodeString.append(chr((ord(Ch) + key - 96) % 26 + 97))
print(''.join(CodeString))