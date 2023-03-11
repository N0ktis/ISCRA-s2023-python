def task1(data):
    to_num = float if "." in data else int
    return sum(to_num(i) for i in data.split(" "))


if __name__ == "__main__":
    assert task1("1 2 3 4 5 6 7") == 28
    assert task1("-1 0.6 15 10000000 0 -1488 -0.0003 23") == 9998549.5997
