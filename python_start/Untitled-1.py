
"""  
Создайте словарь, ключами которого являются буквы английского алфавита,
а значениями – соответствующие им порядковые номера в алфавите.
Для удобства можете воспользоваться модулем string
"""
from string import ascii_letters
string = "pyThonistz"
dict_ = {}
for i in string:
    num = ascii_letters.index(i)+1
    dict_.setdefault(i,num)
print(dict_)