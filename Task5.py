alfavit = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = int(input()) % 26
message = input().upper()
itog = ''
for i in message:
    mesto = alfavit.find(i)
    new_mesto = mesto + key
    itog += alfavit[new_mesto].lower()
print(itog)
