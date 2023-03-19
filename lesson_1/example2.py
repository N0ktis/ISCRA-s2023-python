arraystring = input()
arraystring = arraystring.split(" ")
while True:
    arrayconditions = input()
    word, number = arrayconditions.split("->")
    newarray = []
    for i in arraystring:
        buffer = i.replace(word, number)
        newarray.append(buffer)
    newarray = ' '.join(str(i) for i in newarray)
    print(newarray)
    arraystring = newarray
    arraystring = arraystring.split(" ")
    print("Для выхода напишите exit")