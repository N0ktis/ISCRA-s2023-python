message = input()
while True:
  A = list(input().split('->'))
  if len(A) == 0:
   break
  else:
      message = message.replace(A[0], A[1])
print(message)