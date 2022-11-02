# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на
# указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

number_n = 3
result = 1
lst = list(range(-number_n, number_n+1))
print(lst)
data = open("testex9.txt", "r")
for el in data:
    result *= lst[int(el) - 1]
print(result)

# создание файла в консоли pyCharm^ f = open("testex9.txt", "w", encoding = "utf-8")
# w - создать а - добавить r - прочитать
# f.write("hello") создание текста
# f.flush() f.close() закрыть и записать
# f.seek(0) передвинуть курсор в начало
