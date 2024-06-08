#!/usr/bin/env python3
"""
Module to solve the lockboxes coding problem
"""
from typing import List

def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Returns:
        True, if all boxes can be unlocked
        False, if all boxes can't be unlocked
    """
    # with print assistance
    # print('---------------checking box---------------------')
    # for key in range(1, len(boxes)):
    #     flag = False
    #     print(f'box {key}:')
    #     for box in range(len(boxes)):
    #         print(f'    checking box {box} to find key for box {key}.')
    #         if key in boxes[box] and box != key:
    #             flag = True
    #             print(f"        found key of box {key} in box {box}: {boxes[box]}.")
    #             break
    #     print('done checking')
    #     if not flag:
    #         print(f'box {key} key not found.')
    #         print("=============================")
    #         return False

    # print("=============================")
    # return True
    
    # without print assistance
    for key in range(1, len(boxes)):
        flag = False
        for box in range(len(boxes)):
            if key in boxes[box] and box != key:
                flag = True
                break
        if not flag:
            return False

    return True
