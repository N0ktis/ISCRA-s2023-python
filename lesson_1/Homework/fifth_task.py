ALPHABET = ''.join([chr(i) for i in range(ord('a'), ord('z') + 1)])

string = input()
key = int(input())

print(''.join(map(lambda x: ALPHABET[(ALPHABET.index(x) + key) % len(ALPHABET)] if x in ALPHABET else '', string)))