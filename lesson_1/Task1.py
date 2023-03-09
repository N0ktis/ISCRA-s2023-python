words = list(map(float, input().split()))
print(int(sum(words)) if not (str(sum(words))[-2].isdigit()) else sum(words))
