#!/usr/bin/env python3
# -*- coding: utf-8 -*-

X1 = int(input('Введите x1 '))
Y1 = int(input('Введите y1 '))
X2 = int(input('Введите x2 '))
Y2 = int(input('Введите y2 '))

if X1 == -X2 and Y1 == -Y2:
    print('Точки симметричны относительно начала координат')
elif X1 == -X2 and Y1 == Y2:
    print('Точки симметричны относительно оси Y')
elif X1 == X2 and Y1 == -Y2:
    print('Точки симметричны относительно оси X')
else:
    print('Точки не симметричны')
