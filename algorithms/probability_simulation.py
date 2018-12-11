import numpy as np

length = 200000
total_two_count = 0

for i in range(length):
    two_count = 0
    for i in range(16):
        student = 0
        for j in range(3):
            student += np.random.choice([0, 1], p=[3/8, 5/8])
        if student == 2:
            two_count+=1
    total_two_count += two_count

print(total_two_count/length)

