"""
The Insertion Sort algorithm uses one part of the array to hold the sorted values,
and the other part of the array to hold values that are not sorted yet.

1) Take the first value from the unsorted part of the array.
2) Move the value into the correct place in the sorted part of the array.
3) Go through the unsorted part of the array again as many times as there are values.

"""


import random as rand

# generate random 10 number in array
arr_num = []
for i in range(20):
    # generate random number between 1 to 100 and add in array
    arr_num.append(rand.randint(1,100))

print(arr_num)

arr_len = len(arr_num)

for i in range(1, arr_len):
    if arr_num[i-1] > arr_num[i]:
        temp_ele = arr_num[i]
        for j in range(i-1, -1, -1):
            if arr_num[j] > temp_ele :
                arr_num[j+1] = arr_num[j]
                arr_num[j] = temp_ele

print(arr_num)

"""
Time Complexity = O(n*n) = O(n^2)
"""