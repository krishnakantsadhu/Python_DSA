arr = [3,5,9,1,3,5,7,89,4]

arr_len = len(arr)-1

while arr_len > 0:
    arr[arr_len] = arr[arr_len-1]
    arr_len = arr_len - 1

print(arr)

