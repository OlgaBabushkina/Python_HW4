# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
#  Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов первого множества: "))
list_n = list()
list_m = list()

for i in range (n):
    a = int(input("Введите элемент множества n: "))
    list_n.append(a)

for i in range (m):
    a = int(input("Введите элемент множества m: "))
    list_m.append(a)

set_n = set(list_n)
set_m = set(list_m)
set_result = set_n.intersection(set_m)
list_result = list(set_result)
print(list_result)