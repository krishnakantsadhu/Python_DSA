import random
import timeit

arr_num = []
while len(arr_num) < 10000:
    arr_num.append(random.randint(1,100))

print(arr_num)

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

t1 = timeit.default_timer()
sort_arr = quick_sort(arr_num)
t2 = timeit.default_timer()
print(sort_arr)
print(t2 - t1)

