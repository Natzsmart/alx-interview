#!/usr/bin/python3
'''
calculates the minimum number of operations required
to create a specific number of characters.
Assumes that there are only two operations available:
copying all characters and pasting them
'''


def minOperations(n):
    k = 0

    if n <= 1:
        return k

    for i in range(2, n + 1):
        while (0 == n % i):
            k = k + i
            n = n / i
            if n < i:
                break
    return k
