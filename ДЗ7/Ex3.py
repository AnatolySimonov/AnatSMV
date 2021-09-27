import random
import time


def selection_sort(input_list):
    start_time = time.time()
    for i in range(len(input_list)):
        min_i = i
        for j in range(i + 1, len(input_list)):
            if input_list[min_i] > input_list[j]:
                min_i = j
                input_list[i], input_list[min_i] = input_list[min_i], input_list[i]
    return time.time() - start_time


# Задание 3

list1 = [1000, 2000, 5000, 10000]
for element_in_list in range(len(list1)):
    list2 = []
    for element in range(list1[element_in_list]):
        random_number = random.randint(0, 9)
        list2.append(random_number)
    print(list2)
    print(f'Время сортировки: {selection_sort(list2)} сек.')
    print(f'Длина списка: {len(list2)} элементов.')

'''
Чем больше, тем дольше (c) Жак Фреско
'''
