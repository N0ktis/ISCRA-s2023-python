import math
def main():
    numbers = input().split()
    answer = []
    numbers = list(map(float, numbers))
    for i in numbers:
        answer.append(math.floor(math.fabs(i)))
    for i in answer:
        print(i, end = ' ')

if __name__== '__main__':
    main()