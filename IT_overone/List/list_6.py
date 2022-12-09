# a = 'banama, orange, apple'
# b = a.split(', ')
# print(b)


a = 'banama orange apple'
b = a.split()
r = ''.join(b)
print(b)
print(r)


# a = input().split()
# print(a)


# Выевести только те блюда, которые начинаются с заглавной буквы.
# a = input('Название блюд: ').split()
# print(a)
# for i in a:
#     if i[0].isupper():
#         print(i)


# Создать список с ростом учеников в классе, вывести тех учеников, у кого рост выше, чем у соседа с права.
# a = input('Введите рост: ').split()
# print(a)
# for i in range(len(a)-1):
#     if int(a[i]) > int(a[i+1]):
#         print(a[i])


# Вывести на экран первый, средний и последний элемент из списка.
# a = input('Введите рост: ').split()
# print(a)
# v = len(a) / 2
# v = round(v)
# print(v)
# for i in range(0,len(a),v):
#     print(a[i])


# Создать список с результатами олимпиады по программированнию. Выведите на экран результаты первых трех мест.
# import random
# d = []
# for i in range(10):
#     a = random.randint(1,10)
#     d.append(a)
# print(d)
# d.sort(reverse=True)
# print(d[0:3])


# Создать список в котором хранятся название столиц различных стран, затем вывести его на экран. Попросить
# пользователя ввести столицу которой нет в списке и добавить ее в конец списка. Проверить все элементы списка,
# если длина какого-то элемента меньше 5 удалите его и выведите список на экран.
# capitals = ['Минск', 'Москва', 'Киев']
# print(capitals)
# a = input('Введите столицу, которой нет в списке: ')
# capitals.append(a)
# print(capitals)
# for i in capitals:
#     if len(i) < 5:
#         capitals.remove(i)
# print(capitals)


# Задание №1:
# Дан произвольный список. Представьте его в обратном порядке.
# a = [5,[1,2],2,'r',4,'ee']
# for i in reversed(a):
#     print(i, end=' ')


# Задание №2:
# Дан список некоторых целых чисел, найдите значение 20 в нем и, если оно присутствует замените его на 200.
# Обновите список только при первом вхождении числа 20.
# a = [4,6,23,54,20,11,7,20]
# for i in range(len(a)):
#     if a[i] == 20:
#         a.remove(20)
#         a.insert(i,200)
#         break
# print(a)


# Задание №3:
# Список из 7 цифр. Если четных в нем больше чем нечетных, то найти сумму всех его цифр, если нечетных больше,
# то найти произведение 1 3 и 6 элемента.
# a = [3,6,4,2,4,5,7,3,1]
# g = 0 # сумма всех его цифр
# c = 0 # счетчик четных чисел
# b = 0 # счетчик нечетных чисел
# for i in range(0,len(a)):
#     g += a[i]
#     if a[i] % 2 == 0:
#         c += 1
#     else:
#         b += 1
# print(c,b)
# if c > b:
#     print(g)
# else:
#     print(a[1]*a[3]*a[6])


# Задание №4:
# Найти совпадающие элементы двух списков. Эти значения записать в новый список.
# a = [5,[1,2],2,'r',4,'ee']
# b = [4,'we','ee',3,[1,2]]
# c = []
# for i in range(len(a)):
#     for j in range(len(b)):
#         if a[i] == b[j]:
#             c.append(a[i])
# print(c)


# Задание №5:
# Даны 2 списка. Выполнить следующие операции: 1) Сложить два списка, 2) Добавить элемент 6 на 3 позицию,
# 3) Удалите все текстовые переменные, 4) Посчитайте кол-во элементов списка.
# a = [4,6,'py','tell',78]
# b = [44,'hello',56,'exept',3]
# c = a + b
# print(c)
# c.insert(3,6)
# print(c)
# t = []
# for i in range(0,len(c)):
#     if (isinstance(c[i], int)):
#         t.append(c[i])
# print(t)
# print(len(t))


# Задание №6:
# Дан список. Все числа этого списка проверить на четность. Если число четное, то посчитать сумму его цифр.
# Если нечетное, то заменить его на 1 в списке. Все слова: посчитать количество гласных и согласных.
# Вывести все на экран.
# def words(wordsList):
#     count = 0  # количество гласных
#     for i in range(len(wordsList)):
#         count = 0
#         for vowel in 'aeiouy':
#             count += wordsList[i].count(vowel)
#         print('Количество гласных в слове:', wordsList[i], count, 'согласных:', len(wordsList[i]) - count)
#
# def numbers(numbersList):
#     cnt = 0
#     f = []  # резулитат операции с числами
#     for i in range(len(numbersList)):
#         cnt = numbersList[i] % 2
#         if cnt == 0:
#             t = numbersList[i] // 10
#             y = numbersList[i] % 10
#             e = t + y
#             f.append(e)
#         else:
#             f.append(1)
#     print('Резулитат операции с числами:', f)
#
# list = [15,48,'hello',6,19,'world']
# listInt = [] # список из чисел
# listStr = [] # список из строк
# for i in range(len(list)):
#     if (isinstance(list[i], str)):
#         listStr.append(list[i])
#     if (isinstance(list[i], int)):
#         listInt.append(list[i])
#
# words(wordsList=listStr)
# print(listInt)
# numbers(numbersList=listInt)


