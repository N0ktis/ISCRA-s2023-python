nums = input()  # Ввод данных из консоли
result = 0.0
nums = nums.split()  # Получим список разделив строку по пробелам

for num in nums:
    num = float(num)  # Преобразуем строки в числа с плавающей точкой
    num **= 2  # возводим число в квадрат
    result += num

if int(result) == result:  # Проверяем, является число целым
    result = int(result)  # Для целых чисел меняем тип с float на int

print(result)  # Выводим результат на консоль
