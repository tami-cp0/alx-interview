#!/usr/bin/python3


def isWinner(x: int, nums: list[int]) -> str:
    """
    Determines the winner of the game based on the number
    of rounds and the given numbers.

    Parameters:
        x (int): The number of rounds.
        nums (list[int]): list of integers for each round.

    Returns:
        str: Name of the player who won the most rounds,
        or None if there's a tie.
    """
    players = {'Maria': 0, 'Ben': 0}  # Maria starts first, Ben second
    cummulative = 0

    for n in nums:
        num_list = list(range(1, n + 1))
        toggle = True  # True for Maria's turn, False for Ben's turn

        while num_list:
            prime_found = False
            for number in num_list:
                if check_prime(number):
                    num_list = parse(number, num_list)
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

    if cummulative % 2 == 0:
        return None
    else:
        return max(players, key=players.get)


def check_prime(number: int) -> bool:
    """
    Checks if a number is a prime number.

    Parameters:
        number (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number > 1:
        for i in range(2, (number // 2) + 1):
            if (number % i) == 0:
                return False
        # number is a prime number
        return True

    return False


def parse(number: int, num_list: list[int]) -> list[int]:
    """
    Finds all multiples of a number in a given list and removes them.

    Parameters:
        number (int): The number whose multiples are to be removed.
        num_list (list[int]): The list of numbers to process.

    Returns:
        list[int]: The list after removing multiples of the number.
    """
    return [num for num in num_list if num % number != 0]
