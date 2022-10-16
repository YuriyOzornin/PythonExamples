# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

num: int = int(input("введите число: "))
ist = False
if (num % 5 == 0 or num % 10 == 0 and num % 15 == 0) and num % 30 != 0:
    ist = True
print(ist)
