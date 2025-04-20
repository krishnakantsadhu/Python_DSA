"""
compute sum of the first n terms (where n>0) of series
s = 1-3+5-7+9- .....


ele 1 --> (-1 ^ (1-1) ) (2 * (1-1) + 1)
ele 2 --> (-1 ^ (2-1) ) (2 * (2-1) + 1)
ele 3 --> (-1 ^ (3-1) ) (2 * (3-1) + 1)
....     .....
ele n --> (-1 ^ (n-1) ) (2 * (n-1) +1)

"""

n=int(input("Number of terms in series : "))

sum_series = 0
for i in range(1, n+1):
    ele = ((-1)**(i-1)) * ((2*(i-1)) + 1 )
    print(ele,end=",")
    sum_series = sum_series + ele

print(f"\nSum of {n} terms of series = {sum_series}")