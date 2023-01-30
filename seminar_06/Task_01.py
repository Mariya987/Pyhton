# 1. Представлен список чисел. 
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Use comprehension.

# from random import sample

# def previous(num):
#     my_list = sample(range(num * 3), num)
#     print(my_list)
#     return [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]

# print(previous(int(input())))

result_list = []
list = [int(i) for i in input("Введите список чисел: ").split()]
for i in range(1, len(list)):
    if list[i] > list[i-1]:
        (result_list.append(list[i]))
print("Исходный список: ", list)
print("Список, элементы которого больше предыдущего: ", result_list)