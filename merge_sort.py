import timeit

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]  
                i += 1
            else:
                arr[k] = right[j]  
                j += 1
            k += 1

       
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr


stmt = "merge_sort([5, 2, 9, 1, 5, 6])"
setup = "from __main__ import merge_sort"

execution_time = timeit.timeit(stmt, setup=setup, number=4)
print(f"Execution time: {execution_time} seconds")
