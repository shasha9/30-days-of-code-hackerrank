#Task
#Given an array, A , of N integers, print A's elements in reverse order as a single line of space-separated numbers.

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
arr.reverse()
for i in range(n):
    print(arr[i], end=" ")
