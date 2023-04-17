def f1(n):
    return float(n)**2


if __name__ == "__main__":
    # text = '2 -5 -12 0.33 7 2'
    text = input()
    print(sum(map(f1, text.split())))