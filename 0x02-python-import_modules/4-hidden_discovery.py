#!/usr/bin/python3
import hidden_4

for item in dir(hidden_4):
    if item[0] == "_":
        continue
    else:
        print(item)
