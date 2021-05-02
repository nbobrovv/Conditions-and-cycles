#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    n = int(input("Введите количество экзаменов "))

    if n == 1:
        print('Мы успешно сдали', n, "экзамен")
    elif n == 2 or n == 3 or n == 4:
        print('Мы успешно сдали', n, "экзамена")
    else:
        print("Мы успешно сдали", n, "экзаменов", file=sys.stderr)
        exit(1)
