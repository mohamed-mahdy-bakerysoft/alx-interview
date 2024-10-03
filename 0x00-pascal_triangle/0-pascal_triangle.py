#!/usr/bin/python3
"""
0_pascal_triangle.py
"""


def pascal_triangle(n:int):
    """
    This is a function to plot a designated Pascal Triangle,

    @n: rows in Pascal Triangle
    """
    pas_cal = [[1]] # The base case with one value in the row

    if n > 0:
        for i in range(n - 1):
            inter_array = [0] + pas_cal[-1] + [0]
            new_row = []
            for j in range(len(pas_cal[-1]) + 1):
                new_row.append(inter_array[j] + inter_array[j + 1])
            pas_cal.append(new_row)
        return pas_cal
