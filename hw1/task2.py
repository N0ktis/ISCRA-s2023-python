strline = input()
while True:
    strule = input().split('->')
    strline = strline.replace(strule[0], strule[1])
    print(strline)
