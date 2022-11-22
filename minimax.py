######## Problem
# Given the positive integers, find the minimum and maximum values that can be
# calculated by summing exactly four of the five integers. Then print the minimum
# and maximum values as a single line of two space seperated long integers.
# For example arr = [1,3,5,7,9], minimum sum is 1 + 3 + 5 + 7 = 16
# and maximum sum is 3 + 5 + 7 + 9 = 24
#

# Time complexity
# O(1): order of 1 or constant time, like 2 + 3
# O(log n): means splitting the inputs each step, like deviding it by 2
# O(n): is order over n, like single for loop
# O(n^2): order to power n**2, double for loop over "n" size

import math, os, random, re, sys

def miniMaxSum(arr):
    arr_1 = arr.copy()
    arr_1 = sorted(arr_1)
    return sum(arr_1[:-1]), sum(arr_1[1:])

if __name__ == "__main__":
    arr = list(map(int, input().rstrip().split()))
    print(f'{miniMaxSum(arr)[0]} {miniMaxSum(arr)[-1]}')
