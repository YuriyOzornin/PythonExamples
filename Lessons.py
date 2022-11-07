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

#перед строкой ставится символ r

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
def f():
    x = 2
print(f() is None)