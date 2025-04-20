import numpy as np
i = 1
door = np.zeros(100)
while i <= len(door):
    j = i
    while j <= len(door):
        if j % i == 0:
            if door[j-1] == 0:
                door[j-1] = 1
            else:
                door[j-1] = 0
        j = j + 1
    i = i + 1

for ind, i in enumerate(door):
    if i == 0:
        print(f"Door_{int(ind+1)} closed")
    else:
        print(f"Door_{int(ind+1)} opened")
