# !/usr/bin/evn python3
# -*- config: utf-8 -*-


# Дан список X из n вещественных чисел. Найти минимальный элемент списка, используя
# вспомогательную рекурсивную функцию, находящую минимум среди последних элементов
# списка , начиная с n-гo.


def minimum(a, start):
    min = start
    if a > len(lst):
        print(f"Минимальный элемент: {min}")
        return min
    elif lst[a - 1] < min:
        min = lst[a-1]
    minimum(a + 1, min)


if __name__ == '__main__':
    lst = list(map(float, input("Ввод элементов  ").split(" ")))
    n1 = int(input("Введите номер с самого начала "))
    minimum(n1, lst[n1 - 1])
    
