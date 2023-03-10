string = input()
array = string.split()
result = 0
for el in array:
    if el.find('.') != -1:
        result = result + float(el)
    else:
        result = result + int(el)
print (result)