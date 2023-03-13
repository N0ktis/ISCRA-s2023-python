#problem_2
text = input()
rules = []
while(True):
    x = input()
    if x == '':
        break
    rules.append(x)
for rule in rules:
    x = rule.split("->")
    text = text.replace(x[0], x[1])
    print(text)