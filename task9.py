# Задача: Требуется найти в массиве A[N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Ввод: 5
# Ввод: 1 2 6 4 9
# Ввод: 8
# -> 9

from random import randint
input_set = [randint(1, 50) for i in range(int(input('Введите количество элементов в массиве: ')))]
print(input_set)
x = int(input('Введите число х: '))
input_set = set(input_set)
dif = 0
if x > max(input_set):
    print(max(input_set))
elif x < min(input_set):
    print(min(input_set))
else:
    while True:
        if x - dif in input_set and x + dif in input_set and x - dif != x + dif:
            print(x - dif, x + dif)
            break
        elif x - dif in input_set:
            print(x - dif)
            break
        elif x + dif in input_set:
            print(x + dif)
            break
        else:
            dif += 1