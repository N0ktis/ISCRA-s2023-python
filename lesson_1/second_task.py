main_string = input()
rules = []

while True:
    replace_rule = input()
    if replace_rule == '':
        break
    rules.append(replace_rule)

for elem in rules:
    main_string = main_string.replace(elem.split('->')[0], elem.split('->')[1])
    print(main_string)

'''
main_string = input()

while True:
    replace_rule = input().split('->')
    if replace_rule[0] == 'Thank you, Bro!':
        break
    main_string = main_string.replace(replace_rule[0], replace_rule[1])
    print(main_string)
'''


