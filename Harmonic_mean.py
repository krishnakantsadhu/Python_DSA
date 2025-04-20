"""
Harmonic Mean
H = n / (1/1 + 1/2 + 1/3 ..... 1/n)

"""
from statistics import harmonic_mean

n = int(input("Enter count (n) : "))

sum_result = 0
for i in range(1, n+1):
    sum_result = sum_result + 1 / i

h_mean = n / sum_result

print(f"Harmonic Mean of {n} numbers are {h_mean}")