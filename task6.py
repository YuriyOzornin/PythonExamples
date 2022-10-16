"""
Напишите программу, которая принимает на вход число N
и выдаёт последовательность из N членов.

Пример:
           0    1  2   3   4    #  5
Для N = 5: 1, -3, 9, -27, 81,   # -3**5=-243

"""

# N = int(input("N: "))

N = 5


def sequence(n):
    for i in range(n):
        print((-3) ** i, end=' ')


sequence(N)

