import math
def main():
    numbers = input().split()
    sum = math.fsum(list(map(float, numbers)))
    print(sum)

if __name__== '__main__':
    main()