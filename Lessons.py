# Краткая памятка

# name = input("введите имя: ")
# print("привет,", name)

# print("Yuriy", "Nasty", "Veronika")

# name = "Yuriy"
# print(name)

# isMarried = False
# print(isMarried)

# age = 21
# print("возраст:", age)

# двоичная система
# a = 0b11 
# print(a)

# восьмеричная
# a = 0o7 
# print(a)

# шестнадцатеричная
# a = 0x0A 
# print(a)

# дробные числа
# height = 1.68 
# pi = 3.14
# weight = 68.
# print(height)
# print(pi)
# print(weight)

# комплексные числа
# complexNumber = 1 + 2j
# print(complexNumber)

# строки
# message = "Hello World"
# print(message)

# text = ("oosiuhdfuyfhid"
#         "wuotoiturtwtre")
# print(text)

# text = '''1ueyruyr uyreuuy euryu
# 2euriyuieytr eutyueyt erereer
# 3eufhuy uyeruyu'''
# print(text)

'''
\: позволяет добавить внутрь строки слеш

\': позволяет добавить внутрь строки одинарную кавычку

\": позволяет добавить внутрь строки двойную кавычку

\n: осуществляет переход на новую строку

\t: добавляет табуляцию (4 отступа)
'''

# text = "Message:\n\"Hello World\""
# print(text)

# перед строкой ставится символ r

# path = r"C:\python\name.txt"
# print(path)

'''
Вставка значений в строку
Python позволяет встравивать в строку значения 
других переменных. Для этого внутри строки переменные 
размещаются в фигурных скобках {}, а перед всей строкой 
ставится символ f
'''
# userName = "Tom"
# userAge = 17
# user = f"name: {userName} age: {userAge}"
# print(user)

'''
С помощью встроенной функции type() 
динамически можно узнать текущий тип переменной:
'''

# userId = "abc"      # тип str
# print(type(userId)) # <class 'str'>

# userId = 234        # тип int
# print(type(userId)) # <class 'int'>

# строковые типы данных
# y = "   This is lazy\t\n   "
# удаляем пробелы
# print(y.strip())
# переводим в нижний регистр
# print("DreDre".lower())
# переводим в верхний регистр
# print("attention".upper())
# сопоставляет префикс строки с агрументом
# print("smartphone".startswith("smart"))
# сопоставляет суффикс строки с агрументом
# print("smartphone".endswith("phone"))
# заменяет все вхождения первого аргумента на второй
# print("cheat".replace("ch", "m"))
# склеивает все элементы списка
# print(','.join(["F", "B", "I"]))
# определяет длину строки
# print(len("jfdbjdnbjdjfdknb"))
# содержится ли?
# print("ear" in "earth")

# None означает отсутствие значения
# def f():
#     x = 2
#
# print(f() is None)
# print("" == None)
# print(0 == None)

# списки

# l = [1, 2, 3]
# print(len(l))

# is

# y = x = 3
# print(x is y)
# print([3] is [3])

# Добавление элементов в список

# в конец списка
# l = [1, 2, 2]
# l.append(4)
# print(l)
#
# # вставка
# l = [1, 2, 4]
# l.insert(1, 7)
# print(l)
#
# # конкатенация списков
# print([1, 2, 2] + [5, 8])

# удаление элементов из списка
# l = [1, 2, 5, 8]
# l.remove(1)
# print(l)

# инвертирование списков

# l = [1, 3, 6, 4]
# l.reverse()
# print(l)

# сортировка списков

# l = [2, 1, 4, 2]
# l.sort()
# print(l)
#
# # идексация элементов списка
#
# print([2, 4, 6, 1].index(1))

# стеки

# stack = [5]
# stack.append(34)
# print(stack)
# stack.pop()
# print(stack)
# stack.pop()
# print(stack)

# множества
#
# hero = "Harry"
# guide = "Dublmore"
# enemy = "Lord"
# print(hash(hero))
# print(hash(guide))
#
# # множества строковых значений
#
# characters = {hero, guide, enemy}
# print(characters)

# множества списков создать нельзя

# team_1 = [hero, guide]
# team_2 = [enemy]
# teams = {team_1, team_2}
# error

# все элементы множества должны быть уникальными

# ассоциативные массивы - для хранения данных пар: ключ значение

# calories = {'apple' : 52, 'banana' : 89, 'choco' : 546}
# print(calories['apple'] < calories['choco'])
#
# calories['cappu'] = 74
# print(calories['banana'] < calories['cappu'])
#
# # для доступа ко всем ключам и значениям
#
# print('apple' in calories.keys())
# print(52 in calories.values())
#
# # для доступа к парам ключ значение
#
# for k, v in calories.items():
#     print(k) if v > 500 else None

# принадлежность in
#
# print(3 in [3, 4 ,5])
# print("21" in {"21" , "3"})

# списковое включение (выражение и контекст) for if
# x - идентификатор, x in range(3) - контекст

# [x for x in range(3)]

# customers = [("Jon", 25000),
#              ("Ann", 1000000)]
# whales = [x for x, y in customers if y > 900000]
# print(whales)

# if else elif

# x = int(input("your value: "))
# if x > 3:
#     print("big")
# elif x == 3:
#     print("medium")
# else:
#     print("small")

# циклы for while

# for i in [0, 1, 2]:
#     print(i)

# j = 0
# while j < 3:
#     print(j)
#     j = j + 1
#
# # break
# # continue
#
# #  функции def
#
# def appreciate(x, percentage):
#     return x + x * percentage / 100
# print(appreciate(10000, 5))

# лямбда функции lambda <аргументы> : <возвращаемое выражение>

# print((lambda x: x + 13)(4))