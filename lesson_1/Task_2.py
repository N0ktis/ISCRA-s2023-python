line = input()  # Ввод строки из консоли

while (True):
    replace = input()  # Получаем условия замены символов

    if replace == ':q!':  # Для завершения программы вводим :q!
        break

    replace = replace.split('->')  # Получим список разделив строку по ->
    line = line.replace(replace[0], replace[1])  # Змаеняем символы в строке

    print(line)  # Выводим результат на консоль
