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
