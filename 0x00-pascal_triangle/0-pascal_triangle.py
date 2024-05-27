#!/usr/bin/python3
"""
Pascals triangle
"""
import math

def pascal_triangle(n):
    """
    function that generate the values for a pascal triangle
    """
    values = []

    if n <= 0:
        return values
    
    # for i in range(n):
    #     row = []
    #     print(f"Row number {i}:")
    #     for j in range(i + 1):
    #         print(f"[{i} combination {j}] = ({math.comb(i, j)})", end=" | ")
    #         row.append(math.comb(i, j))
    #     print()
    #     print("===========")
    #     values.append(row)

    for i in range(n):
        row = []
        max = 2**i
        for j in range(i + 1):
            if j > 0:
                row.append(i + j)
        values.append(row)
            




    return values
