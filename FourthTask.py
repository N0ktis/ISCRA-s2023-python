string = input()
array = string.split()
result = 0
for el in array:
    if el.find('.') != -1:
        el = float(el) * float(el)
    else:
        el = int(el) * int(el)
    result = result + el
print (result)