"""
Reverse positive digit number


Algo
----
let num = 1234

num = num/10 | mod 10 | reverse num
-------------|--------|--------------
 1234        | 4      | 4 + 10*0 = 4
 123         | 3      | 3 + 10*4 = 43
 12          | 2      | 3 + 10*43 = 432
 1           | 1      | 1 + 10*432 = 4321
 ------------|--------|-------------------
"""

num = int(input("Enter Number : "))

i = 1
reverse_num = 0
while num > 0:
    reverse_num = num % 10 + (reverse_num * 10)
    num = int(num / 10)


print(reverse_num)
