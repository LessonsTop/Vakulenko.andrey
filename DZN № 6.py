# Задание № 6
# Пункт 1.
# Создать функцию наполнения списка путем ввода данных с клавиатуры.
#
# def add(text, int):
#     # return (text+int)
#     print(text + int)
#
# add(1, 10)
# add("Я учу язык программирования Pyton.", "Это высокоуровневый язык.")
# add("Я учу язык программирования Pyton.", "1234", )
# text1 = "Я учу язык программирования Pyton," "1,2,3,4"
# print(text1.split(","))

# Задание № 6
# Пункт 2
# Создать функцию которая будет перебирать список полученный из функции первого задания
# и вывести только числа из списка на экран.

# my_list = ["Я учу язык программирования Pyton",1,2,3,4,5,6,7,8,9,10]
# list(filter(lambda x: type(x) is int, my_list))
# result = list(filter (lambda x: type(x) is int, my_list))
# print(result if result else "нет там никаких цифр")

# Задание № 6
# Пункт 3
# Создать функцию которая будет генерировать числовые значения в кол-ве 200 шт.,
# затем вывести наибольшее и наименьшее значение из списка.

# from random import randrange
# def listnumbers():
#     number = []
#     for i in range(0,500):
#         number.append(randrange(0,200))
#     print(number)
#     max_number = max(number)
#     min_number = min(number)
#     print("наибольшее число:",max_number)
#     print("наименьшее число:",min_number)
# listnumbers()