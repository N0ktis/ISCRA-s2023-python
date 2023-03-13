line = input()
key = int(input())
line = (chr((ord(s) - ord('a') + key) % 26 + ord('a')) for s in line)
print(''.join(line))
