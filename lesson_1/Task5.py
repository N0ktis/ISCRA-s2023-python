line, numb = input(), int(input())
print(''.join([chr((ord(i) + numb) - 26) if ord(i) + numb > ord('z') else chr((ord(i) + numb)) for i in line.replace(' ', '')]))
