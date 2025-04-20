
"""
series_len = int(input("Enter number of Fibonacci series : >"))

a1 = 0
a2 = 1
while series_len > 0:
    print(a1, end =" ")
    a3 = a2 + a1
    a1 = a2
    a2 = a3
    series_len = series_len - 1

"""
def F(n):
    if n <= 1:
        return n
    else:
        return F(n - 1) + F(n - 2)

for ind in range(0,19):
    print(F(ind), end=" ")

