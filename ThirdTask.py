string = input()
array = string.split()
newString = ''
for el in array:
    if el.find('.') != -1:
        if el.find('-') == 0:
            newString = newString + el[1:el.find('.')] + ' '
        else:
            newString = newString + el[0] + ' '
    else:
        if el.find('-') == 0:
            newString = newString + el[1:] + ' '
        else:
            newString = newString + el + ' '
print (newString)