string = input()
while True:
    replacement = input()
    split_string = replacement.split('->')

    for words in split_string:
        word = split_string[0]
        num = split_string[1]
    replacement_string = string.replace(word, num)
    print(replacement_string)
    string = replacement_string
