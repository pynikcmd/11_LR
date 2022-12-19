#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

def get_input():
    """""
    Запросить строку.
    """""
    return input("Введите строку: ")


def test_input(a):
    """
    Проверить, можно ли данное значение преобразовать к целому числу.
    """
    return a.isdigit()


def str_to_int(b):
    """
    Преобразовать данное значение к целочисленному типу.
    """
    return int(b)


def print_int(c):
    """
    Вывести данное значение на экран.
    """
    print("Это число: ", c)


def main():
    """""
    Главная функция программы
    """""
    stroka = get_input()
    if test_input(stroka):
        print_int(stroka)
    else:
        print("Это не число")


if __name__ == '__main__':
    main()
