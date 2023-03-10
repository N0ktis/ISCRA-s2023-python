string = input()
while True:
    rules = input()
    if rules[0] in string:
        string = string.replace(rules[0], rules[3])
        print (string)
    else:
        break