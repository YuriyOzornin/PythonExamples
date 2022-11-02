# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти
# плоскости, в которой находится эта точка (или на какой оси она находится).

x = int(input("input coordinates of the point x: "))
y = int(input("input coordinates of the point y: "))
if x > 0 and y > 0:
    print("I")
if x < 0 and y > 0:
    print("II")
if x < 0 and y < 0:
    print("III")
if x > 0 and y < 0:
    print("IV")