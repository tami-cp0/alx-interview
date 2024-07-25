#!/usr/bin/python3
"""
Coin change solution
"""

def makeChange(coins, total):
    """
    function to solve the coin change problem
    """
    if total <= 0:
        return 0

    coins = sorted(coins, reverse=True)
    
    for coin in coins:
        if total // coin == 0:
            return total / coin
        
        
    
    