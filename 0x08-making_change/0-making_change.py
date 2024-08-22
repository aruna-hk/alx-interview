#!/usr/bin/python3
"""
    coin denomination
"""


def makeChange(coins, total):
    """
        smallest coin denomination
    """
    no_coins = -1
    if total <= 0:
        return 0
    if len(coins) == 0:
        return no_coins
    coins.sort()
    for i in range(len(coins) - 1, -1, -1):
        rem = total
        Coins = 0
        j = i
        while (j >= 0):
            if (rem >= coins[j]):
                Coins += 1
                rem -= coins[j]
            if (rem < coins[j]):
                j -= 1
            if (rem == 0):
                break
        if (rem != 0):
            Coins = -1
        if (no_coins == -1 or no_coins > Coins):
            no_coins = Coins
    return no_coins
