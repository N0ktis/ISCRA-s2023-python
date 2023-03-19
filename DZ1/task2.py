text = input()
while True:
    rule = input()
    array = rule.split('->')
    print(text.replace(array[0],array[1]))
