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
        while (len(primes) > 0):
            if starter:
                starter = False
                maria += 1
            else:
                starter = True
                ben += 1
            zeroth = primes[0]
            for prime in primes:
                if (prime % zeroth == 0):
                    primes.remove(prime)
    if maria == ben:
        return None
    if maria > ben:
        return "Maria"
    return "Ben"
