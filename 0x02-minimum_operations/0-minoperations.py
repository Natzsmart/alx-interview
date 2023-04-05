#!/usr/bin/python3

def minOperations(n):
    """
    Calculates the minimum number of operations needed to get n H characters in a file.
    
    Args:
    n (int): The desired number of H characters in the file.
    
    Returns:
    int: The minimum number of operations needed to achieve n H characters in the file. If n is impossible to achieve, returns 0.
    """
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