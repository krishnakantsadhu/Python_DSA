import timeit

"""
Operation           Big O Efficiency
--------            ----------------
index []            O(1)
index assignment    O(1)
append              O(1)
pop()               O(1)
pop(i)              O(n)
insert(i, item)     O(n)
del operator        O(n)
iteration           O(n)
contains (in)       O(n)
get slice [x:y]     O(k)
del slice           O(n)
set slice           O(n+k)
reverse             O(n)
concatenate         O(k)
sort                O(n log n)
multiply            O(nk)

"""


def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)


def test3():
    l = [i for i in range(1000)]

# This is fasted way for creating array
def test4():
    l = list(range(1000))

# HELP: https://www.geeksforgeeks.org/timeit-python-examples/
t1 = timeit.timeit(test1,"from __main__ import test1", number=1000)
print(f"{t1:.5f}")

t2 = timeit.timeit(test2,"from __main__ import test2", number=1000)
print(f"{t2:.5f}")

t3= timeit.timeit(test3, "from __main__ import test3",number=1000)
print(f"{t3:.5f}")

t4 = timeit.timeit(test4, "from __main__ import test4",number=1000)
print(f"{t4:.5f}")


