# Задайте список из нескольких чисел. Напишите программу, которая найдет сумму элекментов
# стоящих на нечетной позиции

my_list = [2, 6, 5, 9, 3]
print(sum(i for i in my_list if not i % 2 != 0))