# 3 task

import math

number = input().split()
s = [math.floor(abs(float(ch))) for ch in number]
for x in s:
    print(int(x))
