#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

def multiplication():
    """
    Переножать зачения, пока не будет введен 0.
    """
    a = 1
    while True:
        b = int(input("Введите число: "))
        if b == 0:
            return print(f"Произведение чисел: {a}")
        else:
            a *= b


def main():
    """""
    Главная функция программы
    """""
    multiplication()


if __name__ == '__main__':
    main()
