import random


def mid(arr):
    # Находит среднее арифметическое списка
    l = len(arr)
    ret = arr[0]
    for i in range(1, l):
        ret += arr[i]
    return ret / l

# array generation


n = random.randint(1, 9)
arr = [random.uniform(0, 1) for x in range(n)] # Генерация псевдослучайных чисел в интервале [0, 1]
print("Список случайных чисел:", arr)
# max, min and medium value searching
arr_max = max(arr)
arr_min = min(arr)
arr_mid = mid(arr)
# print a values
print("max value: {}\nmin value: {}\nmid \
    value: {}".format(arr_max, arr_min, arr_mid))
