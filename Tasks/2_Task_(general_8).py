#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

def positive():
    """"
    Вывод: положительное.
    """""
    print("Положительное")


def negative():
    """""
    Вывод: отрицательное.
    """""
    print("Отрицательное")


def test():
    """""
    Ввод числа.
    """""
    a = int(input("Введите целое число: "))
    if a > 0:
        positive()
    elif a < 0:
        negative()
    else:
        print("a = ", a)


def main():
    """""
    Главная функция программы.
    """""
    test()


if __name__ == '__main__':
    main()
