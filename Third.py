# Самый лучшая сортировка в Python - это Timsort. В лучшем случае O(n), в среднем и худшем O(nlogn). Уже встроена в Python (sorted())
# Он стабилен, написан на C и использует insertion sort + merge sort в нужных случаях.

# Пример реализации ниже
def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = i - 1
        while j >= left and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
    return arr

def merge(left, right):
    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    else:
        return [right[0]] + merge(left, right[1:])

def tim_sort(arr):
    min_run = 32
    n = len(arr)
    for i in range(0, n, min_run):
        insertion_sort(arr, i, min(i + min_run - 1, (n - 1)))
    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size
            end = min((start + size * 2 - 1), (n - 1))
            merged_array = merge(arr[start:midpoint], arr[midpoint:end + 1])
            arr[start:start + len(merged_array)] = merged_array
        size *= 2
    return arr
  
a = [5, 3, 1, 4, 6, 2]
sorted_list = tim_sort(a)
print("Sorted list using TimSort:", sorted_list)