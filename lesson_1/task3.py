num_arr = input().split(" ")
for i in num_arr:
    print(int(round(abs(float(i)), 0)), end=" ")
