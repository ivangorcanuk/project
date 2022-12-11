# n = 3
# m = 2
# a = [[i] * m for i in range(n)]
# print(a)


# import random
# Matrix = [[random.randint(1, 11) for j in range(3)] for i in range(2)]
# print(Matrix)


# n = 3
# m = 2
# a = []
# for i in range(n):
#     a.append([i] * m)
# print(a)


# import random
# n = 3
# m = 2
# a = [[random.randint(1,10)] * m for i in range(n)]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         a[i][j] = random.randint(1,10)
#     print(a[i])


# 1. Создать матрицу m на n, где m и n вводятся с клавиатуры. Элементы матрицы заполнять случайными цифрами.
# Сделать читабельный вывод матрицы.
# import random
# n = int(input('Кол-во вложеных списков: '))
# m = int(input('Кол-во элементов во вложеных списках: '))
# a = []
# for i in range(n):
#     b = []
#     for j in range(m):
#         b.append(random.randint(1,10))
#     a.append(b)
#     print(*a[i])


# 2. Матрица n на m, можно задасть статически. Элементы заполняются случайными числами. Вводить с клавиатуры число
# и если оно есть в матрице, то вывести индекс строки и колонки в которой она находится.
# import random
# n = int(input('Кол-во вложеных списков: '))
# m = int(input('Кол-во элементов во вложеных списках: '))
# a = []
# for i in range(n):
#     b = []
#     for j in range(m):
#         b.append(random.randint(1,10))
#     a.append(b)
# print(a)
# b = int(input('Введите число: '))
# for i in range(len(a)):
#     if b in a[i]:
#         print(i,a[i].index(b))
#         break


# 3. Введите 2 числа с клавиатуры. Поделите одно на другое. Обработайте ошибку деления на 0, если ошибок нет,
# то результат деления возвести в квадрат. Так же используйте оператор finally.
# a = [int(i) for i in input().split()]
# try:
#     b = a[0]/a[1]
# except ZeroDivisionError:
#     print('Делить на 0 нельзя')
# else:
#     print(b**2)
# finally:
#     print('Усё')


# 4. Введите 2 числа с клавиатуры. Поделите 1-но на 2-ое. Обработайте ошибку деления на 0, и ошибку
# преобразования в int(), и общее исключение.
# a = input()
# b = input()
# try:
#     c = int(a) / int(b)
# except ValueError:
#     print('Строки не являются числами')
# except ZeroDivisionError:
#     print('На 0 делить нельзя!')
# except:
#     print('Сработало общее исключение')
# else:
#     print(c)


# 5. Матрица 5х5. Найти строку с максимальной суммой элементов и вывести её номер.
# import random
# n = int(input('Кол-во строк: '))
# m = int(input('Кол-во столбцов: '))
# a = [[random.randint(1, 11) for j in range(m)] for i in range(n)]
# print(a)
# c = 0
# v = 0
# for i in range(len(a)):
#     if c < sum(a[i]):
#         c = sum(a[i])
#         v = i
# print('Индекс:', v, '\n'
#       'Сумма:', c)


# 6. Ввод с клавиатуры. Если строка введённая с клавиатуры - это числа, то поделить 1-ое на 2-ое. Обработать ошибку
# деления на 0. Если 2-ое число 0, то программа запрашивает ввод чисел заново. Так же если были введены буквы,
# то обработать исключения.
# while True:
#     a = [i for i in input().split()]
#     try:
#         b = int(a[0]) / int(a[1])
#     except ValueError:
#         print('Строки не являются числами')
#     except ZeroDivisionError:
#         print('Ошибка, на 0 делить нельзя!')
#     else:
#         print(b)
#         break
