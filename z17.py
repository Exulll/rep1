# print('Начало')
# try:
#     number = int(input('Введите число: '))
#     print(f'Ваше число: {number}')
# except:
#     print('Преобразование произошло неудачно')
# finally:
#     print('Все исключения обработаны')
# print('Конец')
# try:
#     print(1/0)
# except ZeroDivisionError:
#     print('Это ошибка значения')
# finally:
#     print('Это будет напечатано в любом случае')
# with open(file, mode) as file_obj:
#     инструкция
# with open('hello.txt', 'w') as my_file:
#     my_file.write('hello world')
# file предоставляет путь к файлу, mode устанавливает режим открытия
# в зависимости от того, что мы собираемся с ним делать
# my_file = open('hello.txt', 'w')
# my_file.close()
# Режимы для работы с файлами:
# r (Read) для чтения, если не найден, то FileNotFoundError
# w (Write) для записи, если отсутствует, то создается, если уже есть, то
# Создается заново, а старые данные стираются
# a (Append) для записи, если отсутствует, то создается, если есть, то записывает данные в конец
# b (Binary) для работы с бинарными файлами, применяется вместе с другими режимами w или r
# try:
#     my_file = open('hello.txt', 'w')
#     try:
#         my_file.write('hello world')
#     except Exception as e:
#         print(e)
# except Exception as Ex:
#     print(Ex)
# with open('hello.txt', 'w', encoding='utf8') as my_file:
#     my_file.write('hello world')
#
# with open('hello.txt', 'a', encoding='utf8') as my_file:
#     my_file.write('\ngoodbye, world')
#
# with open('hello.txt', 'r', encoding='utf8') as my_file:
#     text = my_file.read()
#     print(text)
# file_name.readline() # Считывает одну строку
# file_name.read() # Считывает весь файл
# file_name.readlines() # Считывает все строки файла
# with open('hello.txt', 'r', encoding='utf8') as my_file:
#     while True:
#         x = my_file.readline()
#         print(x)
#         if x == '':
#             break

# with open('z17z2.txt', 'a', encoding='utf8') as z23:
#     while True:
#         a = input()
#         if a == '':
#             break
#         z23.write(a + '\n')
# with open('z17z2.txt', 'r', encoding='utf8') as z4:
#     a = z4.read()
#     print(a)

from z17L2 import a2 as z5a2

a2 = list(map(int, input().split()))
name = input()
a2a5 = list(set(a2) & set(z5a2))
with open(name + '.txt', 'w', encoding='utf8') as z5:
    z5.write('Случайный список:' + str(z5a2) + '\n')
    z5.write('Мой список:' + str(a2) + '\n')
    z5.write('Совпадающие элементы:' + str(a2a5) + '\n')


