#!/usr/bin/python3
for i in range(0, 26):
    print("{:c}".format((ord('z') - i) - (32 * (i % 2))), end="")
