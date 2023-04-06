#!/usr/bin/python3
"""
Calculates the minimum number of operations required to 
create a specified number of characters.
Assumes that there are only two operations available: 
copying all characters and pasting them.
"""

def minOperations(n):
    
    operations = 0

    if n <= 1:
        return operations

    for i in range(2, n + 1):
        while 0 == n % i:
            operations += i
            n //= i
            if n < i:
                break

        return operations