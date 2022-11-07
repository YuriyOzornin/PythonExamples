# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве
from math import sqrt

print("input x and y Point a")
x_a = float(input("X: "))
y_a = float(input("y: "))
print("input x and y Point b")
x_b = float(input("X: "))
y_b = float(input("y: "))
interval = sqrt(((x_b - x_a) ** 2) + ((y_b - y_a) ** 2))
print(interval)

