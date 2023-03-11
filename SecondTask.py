string = input()
while True:
    rules = input()
    if rules != 'end':
        string = string.replace(rules[0], rules[3])
        print (string)
    else:
        break
