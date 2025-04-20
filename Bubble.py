# Bubble sort - The word 'Bubble' comes from how this algorithm works, it makes the highest values 'bubble up'.

import random as rand
# generate random 10 number in array
random_numbers = []
for i in range(10):
    random_numbers.append(rand.randint(1,100))

print(random_numbers)

arr_len = len(random_numbers)

for i in range(arr_len-1):
    for j in range(arr_len-1-i):
        if random_numbers[j] > random_numbers[j+1]:
            temp = random_numbers[j+1]
            random_numbers[j+1] = random_numbers[j]
            random_numbers[j] = temp

print(random_numbers)

"""
Time complexity  O(n^2)
----------------
The Bubble Sort algorithm loops through every value in the array, comparing it to the value next to it. 
So for an array of n values, there must be n such comparisons in one loop.

And after one loop, the array is looped through again and again n times. 
This means there are n * n comparisons done in total, so the time complexity for Bubble Sort is: O(n * n) = O(n^2)

"""
