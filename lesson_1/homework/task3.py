def task3(data):
    return " ".join(i.split(".")[0] for i in data.replace("-", "").split(" "))


if __name__ == "__main__":
    assert task3(("0.23 0 -12 5 -7.11 2")) == "0 0 12 5 7 2"
