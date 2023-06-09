#!/usr/bin/python3
for i in range(100):
    for j in range(i + 1):
        if j // 10 == 0:
            if j % 10 == i // 10 and i % 10 == 0:
                continue
        elif j % 10 == i // 10 and j // 10 == i % 10:
            continue
    if i == 99:
        print("{:02d}".format(i))
    else:
        print("{:02d}".format(i), end=", ")
