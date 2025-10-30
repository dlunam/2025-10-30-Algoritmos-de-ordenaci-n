#Selection Sort 

def selection_sort(my_array):
    n = len(my_array)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if my_array[j] < my_array[min_index]:
                min_index = j
        min_value = my_array.pop(min_index)
        my_array.insert(i, min_value)
    return my_array



#Segunda parte

import random, time

for n in [1000, 10000, 100000]:
    datos = [random.randint(0, n) for _ in range(n)]
    inicio = time.time()
    merge_sort(datos)
    t_merge = time.time() - inicio

    inicio = time.time()
    quick_sort(datos)
    t_quick = time.time() - inicio

    print(f"N={n}: MergeSort={t_merge:.4f}s, QuickSort={t_quick:.4f}s")
