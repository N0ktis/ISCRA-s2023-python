String = input()
while True:
    role = input()
    if role == '':
        break
    old = role[0]
    new = role[3]
    String = String.replace(old, new)
    print(String)