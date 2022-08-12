"""
Декоратор - это функция, которая расширяет
функционал другой функции, не изменяя ее кодовую базу

Функция высшего порядка - это функция, которая принимает и,
или возвращает функцию как переменную

"""

# def func1():
#     print('first')

# def func2():
#     print('second')

# func1()
# func2()

# def func3():
#     print('he')
# def func4(func):
#     func()
#     print('llo')
# func4(func=func3)

# def func():
#     def func1():
#         print('hel')

#     func1()
#     print('lo')
# func()


# def func1():
#     def func2():
#         return 'say hi'
#     print('hi')
#     return func2

# func = func1()
# print(func())

# def decorator(func):
#     def wrapper():
#         print('i runing before main func')
#         func()
#         print('i running after main func')
#     return wrapper

# def main():
#     print("i'm main func")

# decorator_main = decorator(main)
# decorator_main()

# def decorator(func):
#     def wrapper():
#         print('i runing before main func')
#         func()
#         print('i running after main func')
#     return wrapper


# @decorator
# def main():
#     print("i'm main func")
# main()

# def decorator_count(func):
#     def wrapper(name, last_name):
#         print('Количество участников: 12')
#         func(name,last_name)
#     return wrapper

# @decorator_count
# def main(name: str, last_name: str):
#     print(f"{name.capitalize()}{last_name.capitalize()}")
# main('python', 'dor')



# def dec_func(func):
#     def wrapper():
#         print('hello')
#         func()
#         print('hello')
#     return wrapper

# def decorator(func):
#     def wrapper():
#         print('say hi')
#         func()
#         print('say hi')
#     return wrapper

# @dec_func
# @decorator
# def main():
#     print('hi')


# main()

from datetime import datetime

def time_check(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        func(*args, **kwargs)
        end_time = datetime.now()
        print('время выполнения задачи = ')
        print(end_time-start_time)
    return wrapper
@time_check
def generate_range(*args, **kwargs):
    for i in range(args[0]):
        pow(args[1],57556)

generate_range(99,1234523452345)
