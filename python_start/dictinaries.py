"""Cловари - dictionaries"""
"""
Cловарь - изменяемый, итерируемый. 
Состоят из пар: ключ: значение. 
Ключи могут быть только неизменяемыйе типы данных: turple, str, int, None, bool.
А значениями - любые.
Ключи должны быть уникальными, но если есть одинаковые ключи с разными значениями, 
то последний ключ обновит первый
"""

from operator import contains


dict_ = {} #Первый метод создания словаря ключевой синтаксис "{}"
passport = {
    'name': 'Tilek',
    'last_name': 'Esenaliev', 
    'age': 18, 
    'gender': 'male', 
    'birthday': '23.10.2004'
}
#Второй метод создания словаря с вызовом функции "dict()"
dict2 = dict(name='Эльнур', last_name='Эсеналиева') 
#Третий метод создания словаря с вызовом метода "fromkeys" из класса "dict"
dict3 = dict.fromkeys(['key1', 'key2'], 25)
dict4 = dict.fromkeys(['key1', 'key2'])
#Четверый метод создания словаря передачей кортежа
dict5 = dict([('name', 'Данияр'), ('last_name', 'Бийбосунов')])

dict6 = {'a': 50, 'b': 20}
dict6['c'] = 30
dict6['a'] = 40

passport['name']

print(passport.get('name'))
print(passport.get('ID'))

print(passport['name']) #Возвращает 'Tilek'
print(passport['age']) #Возвращает '18'
print(passport['gender']) #Возвращает 'male'
print(passport) #Возвращает весь словарь
print(dict2.get('ID', 'Такого ключа нет'))
print(dict2.setdefault('ID', 'такого ключа не было, но мы создали и он содержит эту строку'))
print(passport.update(dict2))
print(passport) #Возвращает весь словарь
print(dict6)
dict6.pop('d', 'нет такого ключа')
print(dict6)

print(dict6.popitem())
for i in dict6:
    print(dict6[i])

for i in dict6:
    print(i) 

"""keys(), values(), items()"""

for i in dict6.values():
    print(i)
for i in dict6.keys():
    print(i)
for i in dict6.items():
    print(i)

for key, value in dict6.items():
    print(f'ключи - {key} значения - {value}')
contacts = {
    'names': {
        'Tilek': 701460007,
        'Jamin': 500413314
    }
}
print(contacts['names']['Tilek'])
names = contacts['names']
print(names['Tilek'])


