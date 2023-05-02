def cesar_scheme(text, num):
    a_num = ord('a')
    alph_num = ord('z') - a_num + 1
    s = ''
    for i in text:
        i_num = ord(i)
        s += chr(((i_num - a_num + num) % alph_num) + a_num)
    return s


if __name__ == "__main__":
    text = input()
    print(cesar_scheme(text, 7))