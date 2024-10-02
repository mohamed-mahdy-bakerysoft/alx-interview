#!/usr/bin/python3
"""
0-pascal_triangle.py
"""


def pascal_triangle(n:int):
    """
    This is a function to plot a designated Pascal Triangle,

    @n: rows in Pascal Triangle
    """
    pasCal = [[1]] # The base case with one value in the row

    if n > 0:
        for i in range(n - 1):
            interArray = [0] + pasCal[-1] + [0] 
            newRow = []
            for j in range(len(pasCal[-1]) + 1):
                newRow.append(interArray[j] + interArray[j + 1])
            pasCal.append(newRow)
        return pasCal
