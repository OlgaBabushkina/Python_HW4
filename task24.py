# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
#  Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

n = int(input("Введите количество кустов на грядке: "))
list_n = list()
for i in range (n):
    a = int(input("Введите количество ягод на каждом кусте: "))
    list_n.append(a)
print(list_n)
max = list_n[0] + list_n[1] + list_n[2]
for i in range(n):
    if i < n - 3:
        if list_n[i] + list_n[i + 1] + list_n[i + 2] > max:
            max = list_n[i] + list_n[i + 1] + list_n[i + 2]
    elif i < n - 2:
        if list_n[i] + list_n[i + 1] + list_n[-1] > max:
            max = list_n[i] + list_n[i + 1] + list_n[-1]
    else:
        if list_n[i] + list_n[1] + list_n[0] > max:
            max = list_n[i] + list_n[1] + list_n[-1]
print(max)