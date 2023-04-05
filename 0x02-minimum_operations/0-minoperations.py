#!/usr/bin/python3

'''Computes the fewest number of operations needed to result
in exactly n H characters.
'''


def minOperations(n):
    if n == 1:
        return 0
    operations = 0
    currHs = 1
    buffer = 0
    while currHs < n:
        if n % currHs == 0:
            buffer = currHs
        currHs += buffer
        operations += 1
    return operations
