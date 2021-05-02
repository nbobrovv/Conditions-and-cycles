#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    d = int(input('Введите день: '))
    m = int(input('Введите месяц: '))
    y = int(input('Введите год: '))
    x = 0

    bb = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for i in range(m - 1):
        x += bb[i]

    x += d

    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        x += 1

    print("Прошло дней с начала года: ", x)