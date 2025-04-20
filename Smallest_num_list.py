import random as rand

random_numbers = []
for i in range(0,10):
    random_numbers.append(rand.randint(1,100))

print(random_numbers)

# Find smallest number in random array

small_num = random_numbers[0]
ind = 1
while ind < len(random_numbers):
    if random_numbers[ind] < small_num:
        small_num = random_numbers[ind]
    ind = ind + 1
print("Smallest number in array is "+ str(small_num))

"""
Time complexity : O(n)

In this example, the time the algorithm needs to run is proportional, or linear, to the size of the data set. 
This is because the algorithm must visit every array element one time to find the lowest value. 
The loop must run 5 times since there are 5 values in the array. 
And if the array had 1000 values, the loop would have to run 1000 times.

"""