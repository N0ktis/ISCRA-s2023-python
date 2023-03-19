unencrypted_string = input().lower()
key = int(input())

while key >= 26:
    key = key - 26

unencrypted_string = unencrypted_string.replace(' ',
                                                chr(ord('a') + ((ord('u') - key) % (ord('z') + 1)) % ord('a')))

for i in range(len(unencrypted_string)):
    unencrypted_string = unencrypted_string[:i] \
                         + chr(ord('a') + ((ord(unencrypted_string[i]) + key) % (ord('z') + 1)) % ord('a')) \
                         + unencrypted_string[i + 1:]
print(unencrypted_string)
