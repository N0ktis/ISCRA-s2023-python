inp = input('Enter string: ')
repl = input('Enter replace: ')
while '->' in repl:
    print(inp.replace(repl.split('->')[0], repl.split('->')[1]))
    repl = input('Enter replace: ')
