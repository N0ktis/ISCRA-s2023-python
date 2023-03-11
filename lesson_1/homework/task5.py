from string import ascii_lowercase

"""
Aleksey Zhurin, [3/10/2023 12:30 AM]
1) только латиница
2) верхний и нижний регистр считаем взаимозаменяемыми
"""


def task5(data, key):
    data = data.lower()

    result = [
        ascii_lowercase[(ascii_lowercase.index(el) + key) % len(ascii_lowercase)]
        for el in data
        if el in ascii_lowercase
    ]
    return "".join(result)


if __name__ == "__main__":
    # print(task5(input(), int(input())))
    assert task5("i am atomic", 7) == "phthavtpj"
