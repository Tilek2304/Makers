"""Работа с файлами"""

# операции над файлами:
# 1. Чтение 
# 2. Запись

# файлы бывают текстовыми и бинарными

# open(путь_до_файла, режим_работы) - функция для открытия файла

# file = open('test.txt', 'r')
# print(file.read())
# file.close()

"""
r - чтение
w - запись, создает файл, перезаписывает содержимое файла, если такой файл  существует
x - запись, если файла нет, иначе исключение
а - дозапись
w+,r+ - открывает запись и чтение
b - открытие бинарных файлов
t - открытие текстового файла
rt - чтение текстового файла, режим по умолчанию

"""
# file = open('test.txt', 'r')
# print(file.read(5))
# file.close()

# read() - читает весь файл или определенное количество символов,
# если указан аргумент целочисленного типа

# file1 = open('test.txt')
# for i in file1:
#     print(i)
# file1.close()

# file2 = open('test.txt')
# strings = file2.readlines()
# list_ = []
# for word in strings:
#     list_.append(word.strip())

# print(list_)
# file2.close()

# readlines() - читает файл и возвращает список из строк

# jpg = open('watermelon.jpg', 'rb')
# print(jpg.read())
# jpg.close()

# file5 = open('test2.txt')
# print(file5.read())
# file5.seek(0)
# print(file5.read())
# print(file5.tell()) - возвращает местоположение курсора
# file5.close()

# with open('watermelon.jpg', 'rb') as file6:
#     a = 10
#     print(file6.read())
# print(a)

# with function() as var_name: - контекстный менеджер
#     body

# try:
#     file6.read()
#     file6.seek(0)
# finally:
#     file6.close()

# with open('test3.txt', 'w') as f:
#     f.write('GLHF\n')
#     f.write('GLHF\n')
#     f.write('GLHF\n')
#     f.write('GLHF\n')
#     f.write('GLHF\n')

# with open('test4.txt', 'w+') as fi:
#     list_ = ['good', 'luck', 'and', 'have', 'fun']
#     n = [name+'\n' for name in list_]
#     fi.writelines(n)
#     fi.seek(0)
#     print(fi.read())

