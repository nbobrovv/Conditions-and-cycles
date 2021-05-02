
if __name__ == '__main__':
    d = int(input('Введите день: '))
    m = int(input('Введите месяц: '))
    y = int(input('Введите год: '))

    cc = y % 4 == 0 and y % 100 != 0 or y % 400 == 0
    bb = [31, 28 + int(cc), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    print(sum(bb[:m - 1]) + d)