#!/usr/bin/python3
""" prme game """


def isWinner(x, nums):
    """prime game """

    maria, ben = 0, 0
    for i in range(x):
        starter = True
        if i > len(nums) - 1:
            break
        primes = [m for m in range(2, nums[i] + 1)]
        if len(primes) == 0:
            starter = False
        while (len(primes) > 0):
            zeroth = primes[0]
            for prime in primes:
                if (prime % zeroth == 0):
                    primes.remove(prime)
            if len(primes) == 0 and starter is True:
                starter = False
            else:
                starter = True
        if starter:
            maria += 1
        else:
            ben += 1
    if maria == ben:
        return None
    if maria > ben:
        return "Maria"
    return "Ben"
