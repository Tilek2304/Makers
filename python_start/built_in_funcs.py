"""Встроенные функции"""
# print()

# int()
# str()
# float()
# dict()
# list()
# set()
# tuple()
# bool()
# complex()

# pow()
# divmod()

# dir() - возвращает список атрибутов и методов переданного объекта
# type()
# id()
# a = 10
# isinstance(a, int)
# len()
# min()
# max()
# sum()
"""
map() filter() enumerate() zip() reduce()

lambda
"""

# map() - принимает функцию и итерируемый объект. 
# Применяет переданную функцию к каждому элементу итер. объекта

# def plus_ten(x):
#     return x+10
# nums = [1,2,3,4,5]
# res = map(plus_ten, nums)
# print(list(res))

# def plus_ten(x,y):
#     return x+y
# nums = [1,2,3,4,5]
# nums2 = [1,2,3,4,5,6]
# res = list(map(plus_ten, nums, nums2))
# print(res)


# nums = [1,2,3,4,5]
# nums2 = [1,2,3,4,5,6]
# res = list((map(lambda word, nums: word+15+nums,nums2,nums)))
# print(res)

# filter(func, Iterable) - принимает функцию и итер. объект. Фильтрует по условию, указанную в функции

# num = [45,34,56,89,0,2,4,34,65,76,87]
# filter_num = list(filter(lambda nums:nums%5==0,num))
# print(filter_num)

# from functools import reduce
# nums = [10,20,30,40,50]
# # def func1(num1,num2):
# #     return num1+num2
# # res1 = reduce(lambda num1,num2:num1+num2,nums)
# # res = reduce(func1,nums)
# # print(res)
# # print(res1)

# min_value = reduce(lambda x,y:x if x<y else y, nums)
# print(min_value)

# a = 'word'
# res = list(enumerate(a))
# print(res)

# a = 'word'
# res = dict(enumerate(a))
# print(res)

# a = ['ws','os','rs','ds']
# res = dict(enumerate(a,start=12))
# print(res)

# zip() - связывает элементы переданных последовательностей
list1 = [1,2,3,4,5]
list2 = ['a','b','c']
list3 = ['tilek', 'timur', 'elya']
zipped_list = list(zip(list1,list2,list3))
print(zipped_list)
lista,listb,listc = list(zip(list1,list2,list3))
print(lista,listb,listc)
