from string import ascii_letters

alphabet = ascii_letters[:26]
line = input()
n = int(input())
for i in line.replace(" ", ""):
    k = (ord(i) - 97 + n) % 26
    print(alphabet[k], end="")
print()


