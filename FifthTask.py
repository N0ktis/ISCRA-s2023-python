string = input()
key = int(input())
alphabet = 'abcdefghijklmnopqrstuvwxyz'
result = ''
i = 0
while i < len(string):
    if string[i] != ' ':
        element = alphabet.find(string[i]) + key
        if element < len(alphabet):
            result = result + alphabet[element]
        else:
            result = result + alphabet[element - len(alphabet)]
    else:
        result = result + 'u'
    i = i + 1
print (result)