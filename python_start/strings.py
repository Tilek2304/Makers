# строки - неизменяемый, упорядоченный, индексируемый тип данных
# str()

from curses.ascii import isupper


string = 'hello'
string2 = "hello"
string3 = """Hello
world"""

stringName = 'helloWorld 123'

stringName.isupper()             # состоит ли строка из символов только верхнего регистра
stringName.islower()             # состоит ли строка из символов только нижнего регистра
stringName.isdigit()             # cocтоит ли строка только из цифр
stringName.isalpha()             # состоит ли строка только из букв
stringName.isalnum()             # состоит ли строка и из букв и из цифр
stringName.isspace()             # состоит ли строка из пробелов
stringName.endswith('123')       # заканчивается ли строка из переданной подстрокой
stringName.startswith('hell')    # начинается ли строка из переданной подстроки





len(stringName)                          #выводит длину строки
stringName.split()                       #делит строку в возвращаемый список используя аргумент, по умолчанию ' '
stringName.replace( 'l','b')             #заменяет букву l на b и возвращает итоговый результат
stringName.upper()                       #возвращает строку полностью в верхнем регистре
stringName.lower()                       #возвращает строку полностью в нижнем регистре
stringName.title()                       #возвращает строку поднимая первую букву каждого слова в верхний регистр
stringName.capitalize()                  #возвращает строку поднимая первую букву в верхний регистр
stringName.casefold()                    # 'ß' - ss - эсцет более агрессивный перевод в нижний регистр
stringName.count()                       #возвращает количество вхождений переданной подстройки
stringName.join('Tilek','hello','bye')   #соединит строки строкой stringName
stringName.strip()                       #убирает символы указанные в аргументе в начале и в конце строки (варианты lstrip() rstrip())

str7 = 'hello world'

#index - порядковый номер символа в строке считая с нуля
# 'makers'
#  012345
# -054321
print(str7[4:])     #от 4 до конца строки 
print(str7[:5])     #от начала до 5
print(str7[0:-1:1]) #от начала до консца с шагом 1
print(str7[::1])    #от начала до консца с шагом -1 т.е. задом наперед
