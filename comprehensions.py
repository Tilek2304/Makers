"""comprehensions (генераторы)"""

# a = []
# for i in range(10):
#     a.append(i)
# print(a)

# list_ = [i for i in range(10)]
# print(list_)

# list2 = [выражение for выражение in итерируемый_объект]



from hashlib import new


names = ['Tilek', 'Aijamal', 'Dastan', 'Bayas']

# names2 = []
# for i in names:
#     names2.append(i+'10')
# print(names2)

# names2 = [i+'10' for i in names]
# print(names2)

# for i in names:
#     if i[0] == 'A':
#         names2.append(i)
# print(names2)

# names2 = [i for i in names if i[0] == 'A']
# print(names2)

nums = [1,2,4,5,5,7,7,34,234,6]
# new_nums = []
# for i in nums:
#     if i%2 == 0:
#         new_nums.append(i+0.6)
#     else:
#         new_nums.append(i+0.3)
# print(new_nums)

new_nums = [i+0.3 if i%2 == 0 else i+0.6 for i in nums]
print(new_nums)
# comprehensions - это более короткий способ записи циклов 
# для создания коллекций (списки, словари, множества, кортежи)
lists  = [[1,2,3], [4,5,6,], [7,8,9]]
# list_ = []
# for i in lists:
#     for j in i:
#         list_.append(j)
# print(list_)

new_list = [j for i in lists for j in i]
print(new_list)