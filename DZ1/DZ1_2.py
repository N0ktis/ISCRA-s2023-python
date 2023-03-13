line = input()
while True:
	rule = input().split('->')
	line = line.replace(rule[0], rule[1])
	print(line)
