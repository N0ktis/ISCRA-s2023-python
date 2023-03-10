# line, numb = input(), int(input())
# print(''.join([chr((ord(i) + numb) - 26) if ord(i) + numb > ord('z') else chr((ord(i) + numb)) for i in line.replace(' ', '')]))

arr, line, numb, ans = [], input(), int(input()), ""
for i in range(97, 123):
    arr.append(chr(i))

for i in line.replace(' ', ''):
    ans += arr[(arr.index(i) + numb) % 26]
print(ans)
