#!/usr/bin/python3
"""
Pascals triangle
"""
# import math

def pascal_triangle(n):
    """
    function that generate the result for a pascal triangle
    """
    result = [[1]]

    if n <= 0:
        return result
    
    # this solves it but uses the math library.
    # for i in range(n):
    #     row = []
    #     print(f"Row number {i}:")
    #     for j in range(i + 1):
    #         print(f"[{i} combination {j}] = ({math.comb(i, j)})", end=" | ")
    #         row.append(math.comb(i, j))
    #     print()
    #     print("===========")
    #     result.append(row)

    for i in range(n - 1):
        # create a row with 0 ... 0
        temp = [0] + result[-1] + [0] 
        row = []
        # loop though the length of the previous row plus 1
        for j in range(len(result[-1]) + 1):
            # calculate the value based on the 2 numbers directly above the
            # row position
            row.append(temp[j] + temp[j + 1])
        # append complete row to result
        result.append(row)

    return result
