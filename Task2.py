line = input()
print('Enter "stop" to stop)')
while True:
    change = input()
    if change == 'stop': break
    else:
        change = change.split('=>')
        line = line.replace(change[0],change[1])
        print(line)
