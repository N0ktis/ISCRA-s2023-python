string = map(lambda x: x.encode('ascii'), input().lower().split())
key = int(input())
print(" ".join([''.join([chr((x+key)%(ord('z')+1)+((x+key)//(ord('z')+1))*ord('a')) for x in y])
                for y in string]))
