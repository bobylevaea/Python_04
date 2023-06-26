# Задача 22: Даны два неупорядоченных набора целых чисел
# (может быть, с повторениями). Выдать без повторений в порядке возрастания
# все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит
# сами элементы множеств.

from random import randint

first_set = int(input("Введите количество элементов первого множества: "))
second_set = int(input("Введите количество элементов второго множества: "))

first_set_list = []
second_set_list = []

for i in range(first_set):
    num = randint(1, 100)
    first_set_list.append(num)

for i in range(second_set):
    num = randint(1, 100)
    second_set_list.append(num)

joined_list = sorted(set(first_set_list + second_set_list))
print(joined_list)