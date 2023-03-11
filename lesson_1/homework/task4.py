def task4(data):
    return sum(float(i) ** 2 for i in data.split(" "))


if __name__ == "__main__":
    assert task4("2 -5 -12 0.33 7 2") == 226.1089
