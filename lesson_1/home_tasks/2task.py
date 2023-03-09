a = input()
while True:
    b = input()
    if b == 'end':
        break
    a = a.replace(b[0], b[3:])
    print(a)
