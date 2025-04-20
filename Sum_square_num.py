
"""
Sum of square of n numbers

"""

count = int(input("Count of number >"))

sum = 0
for i in range(1,count+1):
    sum = sum + (i*i)

print(f"Sum of square of {count} number : {sum}")