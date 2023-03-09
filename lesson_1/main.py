
# print('Hello, world!')

# print('Привет, мир!')


# # line = input()
# # a, b = line.split()
# # a, b = int(a), int(b)
# # print(((3 * a) ** 8 + b * 67 - 98) // 4)
# print(12345**123)


line = input()
words = line.split()
result = sorted((float(word) for word in words), reverse=True)
print(result)

# result = []
# for word in words:
#     result.append(int(word))


# result = list(map(int, words))



# print(words)
# print(result)