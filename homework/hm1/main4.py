#problem5
str = input().replace(' ', '')
key = int(input())
result = ''
for iter in str:
    if ord(iter) < 97:
        iter = chr(ord(iter) + 32)
    iter = chr(( (ord(iter) + key) - 123) % 26 + 97)
    result+=iter
print(result)
