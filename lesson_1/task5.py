unencoded_str = input().replace(" ", "")
key = int(input())
for i in unencoded_str:
    print(chr(96 + (ord(i) + key - 96) % 26), end="")
