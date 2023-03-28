a = input()
b_1, n_1 = input().split(sep='->')
b_2, n_2 = input().split(sep='->')
b_3, n_3 = input().split(sep='->')
total_1 = ''
total_2 = ''
total_3 = ''
for b in a:
    while b == b_1:
        b = n_1
    total_1 += b
print(total_1)
for b in total_1:
    while b == b_2:
        b = n_2
    total_2 += b
print(total_2)
for b in total_2:
    while b == b_3:
        b = n_3
    total_3 += b
print(total_3)
