arraystring = input()
while True:
    arrayconditions = input()
    word, number = arrayconditions.split("->")
    newarray = []
    buffer = arraystring.replace(word, number)
    newarray.append(buffer)
    newarray = ' '.join(str(i) for i in newarray)
    print(newarray)
    arraystring = newarray
    print("Для выхода напишите exit")
