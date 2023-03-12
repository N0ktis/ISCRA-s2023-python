line = input()
line = line.replace(' ','')
print('Key:')
key = int(input())
message = ''
for x in list(line):
    if ord(x) >= 115:
        message = message + chr((ord(x)+key)%122 + 97)
    else:
        message = message + chr(ord(x)+key)
print(message)
#так и не понял из обсуждения в группе, надо сохранять пробелы или нет