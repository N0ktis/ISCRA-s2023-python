#problem5
str = input()
key = int(input())
result = ''
for iter in str:
    iter = chr(ord(iter) + key)
    result+=iter
print(result)