#Определить индексы элементов массива (списка), значения которых принадлежат заданному #диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint
my_list = [randint(0, 100) for _ in range(10)]
print(my_list)
min = int(input("Введите минимальное значение = "))
max = int(input("и максимальное значение диапазона = "))
for item in range(len(my_list)):
    if min < my_list[item] < max:
        print(item)