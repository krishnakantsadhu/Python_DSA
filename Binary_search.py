import random
# random sorted array
# arr_num = [random.randint(i*5, (i+1)*5) for i in range(19) ]
# print(arr_num)

#
# arr_num = [3, 7, 13, 20, 21, 27, 34, 39, 41, 49, 51, 55, 64, 67, 72, 79, 82, 90, 93, 96]
# print(arr_num)
# search_num = 40
# low_idx = 0
# high_idx = len(arr_num)-1
# mi_idx = int((low_idx + high_idx) / 2)
# is_found = False
#
#
# while high_idx - low_idx >= 0:
#     # print(low_idx, mi_idx, high_idx)
#     if arr_num[mi_idx] < search_num:
#         low_idx = mi_idx + 1
#     elif arr_num[mi_idx] > search_num:
#         high_idx = mi_idx - 1
#     else:
#         is_found = True
#         break
#
#     mi_idx = int((low_idx + high_idx) / 2)
#
# if is_found:
#     print(f"Number {search_num} found at index", mi_idx)
# else:
#     print(f"Number {search_num} NOT found")

"""
Time Complexity  : O(log(n))
"""


"""
Binary search using recursion 
"""
def binary_search(s_num, arr,lo,hi):

    if lo > hi:
        return -1

    mi = (lo + hi) // 2

    if arr[mi] < s_num :
        lo= mi + 1
        return binary_search(s_num, arr,lo,hi)
    elif arr[mi] > s_num :
        hi = mi - 1
        return binary_search(s_num, arr,lo, hi)
    else:
        return mi

arr_num1 = [3, 6, 12, 18, 22, 26, 31, 36, 40, 46, 50, 60, 64, 69, 73, 75, 83, 90, 92]
search_num = 90
low_idx = 0
high_idx = len(arr_num1)-1


print(arr_num1)
ind = binary_search(search_num, arr_num1,low_idx,high_idx)
print(ind)


