#! /usr/bin/env python3

# A script for getting the smallest prime factor of an integer.

import sys

def smallest_factor(n):
    """Returns the smallest prime factor of n, or None if n is prime.
    
    Usage:
    smallest_factor(n)
    
    Paramters
    ----------
    param n: int
    A positive integer.
    
    Examples:
    >>> smallest_factor(15)
    3
    >>> smallest_factor(13)
    13

    Returns
    -------
    The smallest prime factor of n, or None if n is prime.
    "int or None"
    """

    smallest_prime_factor = None # Initialize to None, which will be the value if n is prime.
    for i in range(2,n):
        if (n % i) == 0:
            smallest_prime_factor = i
            break

    return smallest_prime_factor 


def get_list_of_primes(n):
    """Returns a list of all prime numbers less than n.
    
    Usage:
    get_list_of_primes(n)
    
    Parameters
    ----------
    param n: int
    A positive integer.
    
    Examples:
    >>> get_list_of_primes(10)
    [2, 3, 5, 7]

    Returns
    -------
    A list of all prime numbers less than n.
    "list of int"
    """

    list_of_primes = []
    for i in range(2,n):
        if smallest_factor(i) is None:
            list_of_primes.append(i)

    return list_of_primes





if __name__ == "__main__":
    if len(sys.argv) != 2: # Expecting exactly one command line argument, which is the integer for which to get the smallest factor.
        sys.exit(sys.argv[0] + ": Expecting one command line argument -- the integer for which to get the smallest factor")
    n = int(sys.argv[1]) # Convert the command line argument to an integer.
    if n < 1:
        sys.exit(sys.argv[0] + ": Expecting a positive integer")
    prime_factor = smallest_factor(n)
    if prime_factor is not None:
        print("The smallest prime factor of", n, "is", prime_factor)
    else:
        print(n, "is prime")

    list_of_primes = get_list_of_primes(n)
    print("The prime numbers less than", n, "are:", list_of_primes)
