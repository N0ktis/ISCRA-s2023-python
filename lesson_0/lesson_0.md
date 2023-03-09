# Занятие 0: гайд по установке Python, PyCharm и Jupyter

Данный гайд содержит инструкцию по установке интепретатора Python3, IDE PyCharm и Jupiter на операционные системы Windows и Linux. 


* [Установка Python](#Установка_Python)  
  * [Windows](#Установка_Python_win)  
  * [Linux](#Установка_Python_linux)  
* [Установка PyCharm](#Установка_PyCharm)  
  * [Windows](#Установка_PyCharm_win)  
  * [Linux](#Установка_PyCharm_linux)  
* [Создание своего первого проекта](#Создание_своего_первого_проекта)  
* [Установка Jupiter](#Установка_Jupiter)  

<a name="Установка_Python"></a>
## Установка Python

Для прохождения курса желательно иметь версию Python 3.8.2 или выше.

<a name="Установка_Python_win"></a>
### Windows
Открываем браузер и переходим по [ссылке](https://www.python.org/).

На странице выбираем последний релиз.

![](https://github.com/N0ktis/ISCRA-python/blob/main/img/1.png)

Листаем в самый низ и скачиваем установочный файл, соотвествующий разрядности вашей операционной системы.

![](https://github.com/N0ktis/ISCRA-python/blob/main/img/2.png)

После скачивания запускаем установщик.  
**ВАЖНО:** нужно обязательно отметить пункт `Add python.exe to PATH`

![](https://github.com/N0ktis/ISCRA-python/blob/main/img/3.png)

Нажимаем кнопку `Install Now` и ждём завешения установки.

Чтобы проверить правильность установки можно запустить PowerShell (или просто командую строку) и ввести команду `python`.  
Должен запуститься интепретатор Python, где будет указана его версия.

![](https://github.com/N0ktis/ISCRA-python/blob/main/img/4.png)

<a name="Установка_Python_linux"></a>
### Linux

Из коробки дистрибутив Ubuntu 22.04 имеет на борту Python 3.10.6

![](https://github.com/N0ktis/ISCRA-python/blob/main/img/8.png)

Данной версии полностью достаточно для нужд курса.  
Если же у вас более низкая версия Python и вы хотите обновиться, то пропишите в командной строке:

```
sudo apt-get upgrade python3
```

<a name="Установка_PyCharm"></a>
## Установка PyCharm

<a name="Установка_PyCharm_win"></a>
### Windows

Переходим по [ссылке](https://www.jetbrains.com/pycharm/download/#section=windows) и скачиваем PyCharm Community Edition.

![](https://github.com/N0ktis/ISCRA-python/blob/main/img/7.png)

<a name="Установка_PyCharm_linux"></a>
### Linux

PyCharm Community Edition можно установить через терминал введя команду:
```
sudo snap install pycharm-community --classic
```
Или скачав и распоковав архив с [сайта](https://www.jetbrains.com/pycharm/download/#section=linux):

![](https://github.com/N0ktis/ISCRA-python/blob/main/img/9.png)

<a name="Создание_своего_первого_проекта"></a>
## Создание своего первого проекта

Запускаем PyCharm и жмём на кнопку `New Project`.

![](https://github.com/N0ktis/ISCRA-python/blob/main/img/11.png)

Указываем имя проекта и версию интепретатора Python.

![](https://github.com/N0ktis/ISCRA-python/blob/main/img/12.png)

Должна создаться папка для нашего проекта.

Щёлкаем правой кнопкой на корневой директории и выбираем создать новый python файл:

![](https://github.com/N0ktis/ISCRA-python/blob/main/img/15.png)

Указываем имя файла и нажимаем `Enter`:

![](https://github.com/N0ktis/ISCRA-python/blob/main/img/16.png)

После создания файла он сразу у нас откроется.

![](https://github.com/N0ktis/ISCRA-python/blob/main/img/17.png)

<a name="Установка_Jupiter"></a>
## Установка Jupiter

Открываем PowerShell или терминал и прописываем следующую команду:

```
pip install notebook
```

Чтобы запустить локально сервер Jupyter вводим в командой строке:

```
jupyter notebook
```
![](https://github.com/N0ktis/ISCRA-python/blob/main/img/13.png)

В браузере должна открыться подобная страничка.

![](https://github.com/N0ktis/ISCRA-python/blob/main/img/14.png)

Чтобы остановить сервер нужно нажать комбинацию `CTRL+C` в командой строке.
