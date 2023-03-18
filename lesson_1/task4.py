import math
def main():
    numbers = input().split()
    answer = []
    numbers = list(map(float, numbers))
    for i in numbers:
        answer.append(math.pow(i, 2))
    print(math.fsum(list(map(float, answer))))

if __name__== '__main__':
    main()