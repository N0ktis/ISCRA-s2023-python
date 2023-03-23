def f1(n):
    return abs(int(float(n)))


if __name__ == "__main__":
    # text = '0.23 0 -12 5 -7.11 2'
    text = input()
    print(*map(f1, text.split()))