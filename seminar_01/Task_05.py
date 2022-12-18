# 5. Напишите программу, 
# которая принимает на вход координаты двух точек и находит
# расстояние между ними в 2D пространстве.
# AB = √(xb - xa)2 + (yb - ya)2

from math import sqrt

firstX = int(input('Введите первую точку X:'))
secondX = int(input('Ввелите вторую точку X:'))
firstY = int(input('Введите первую точку Y:'))
secondY = int(input('Ввелите вторую точку Y:'))
temp = round(sqrt((secondX - firstX)**2 + (secondY - firstY)**2), 2)
print(temp)






    