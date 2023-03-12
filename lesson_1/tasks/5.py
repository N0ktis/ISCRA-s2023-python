string, code = input().replace(' ', ''), int(input())
print(*[chr(ord(i) + code) if (ord(i) + code <= 122) else chr(96 + (code - (ord('z') - ord(i)))) for i in string],
      sep='')
