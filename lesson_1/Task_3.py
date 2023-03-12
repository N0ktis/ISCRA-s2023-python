nums = input()  # Ввод данных из консоли
result = []
nums = nums.split()  # Получим список разделив строку по пробелам

for num in nums:
    num = num.replace('-', '')  # Убираем -
    num = num.replace('+', '')  # Убираем +
    num = num.split('.')  # Разделяем строку по точкам
    result.append(num[0])  # Дописываем в result челую часть числа

result = ' '.join(result)  # Убираем скобки и запятые для вывода на консоль

print(result)  # Выводим результат на консоль
