#!/usr/bin/python3
"""
Define isWineer function, a solution to the Prime Game problem
"""


def isWinner(x, nums):
    """
    Determines the winner of the game based on the number
    of rounds and the given numbers.
    Returns:
        str: Name of the player who won the most rounds,
        or None if there's a tie.
    """
    # Validate inputs
    if not isinstance(x, int) or not isinstance(nums, list):
        return None

    if (
        x < 1 or
        len(nums) != x or
        not nums or
        not all(isinstance(num, int) for num in nums)
    ):
        return None

    players = {'Maria': 0, 'Ben': 0}  # Maria starts first, Ben second
    cummulative = 0

    for n in nums:
        num_list = list(range(1, n + 1))
        toggle = True  # True for Maria's turn, False for Ben's turn

        while num_list:
            prime_found = False
            for number in num_list:
                if check_prime(number):
                    # remove the prime number and multiples of it
                    num_list = [num for num in num_list if num % number != 0]
                    prime_found = True
                    break

            if not prime_found:
                cummulative += 1
                # No prime number left to choose, the current player loses
                if toggle:
                    players['Ben'] += 1
                else:
                    players['Maria'] += 1
                break

            toggle = not toggle  # Switch player turn

    if cummulative % 2 == 0 or cummulative == 0:
        return None
    else:
        return max(players, key=players.get)


def check_prime(number: int) -> bool:
    """
    Checks if a number is a prime number.
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number > 1:
        for i in range(2, (number // 2) + 1):
            if (number % i) == 0:
                return False
        return True  # number is a prime number

    return False
