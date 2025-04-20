# The Selection Sort algorithm finds the lowest value in an array and moves it to the front of the array.

"""
1. Go through the array to find the lowest value.
2. Move the lowest value to the front of the unsorted part of the array.
3. Go through the array again as many times as there are values in the array.
"""

import random as rand

def generate_random_array(size):
    # generate random 10 number in array
    arr = []
    for i in range(size):
        # generate random number between 1 and 100 and add in array
        arr.append(rand.randint(1,100))
    return arr


arr_num=generate_random_array(10)

print(arr_num)

arr_len = len(arr_num)

for j in range(arr_len-1):
    small_num_idx= j
    small_num = arr_num[j]
    # search for smallest number in array.
    for i in range(j, arr_len-1):
        if small_num > arr_num[i+1]:
            small_num_idx = i + 1
            small_num = arr_num[small_num_idx]

    # swapping the smallest element with first element of unsorted part of array
    swap = arr_num[j]
    arr_num[j] = arr_num[small_num_idx]
    arr_num[small_num_idx] = swap

print(arr_num)

"""
Time complexity  O(n*n) = O(n^2)
----------------

"""
