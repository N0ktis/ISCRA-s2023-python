import math

num_arr = input().split(" ")
for i in num_arr:
    print(int(math.floor(abs(float(i)))), end=" ")
