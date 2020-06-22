#Task
#Sort a given array using Bubble Sort algorithm.

import sys


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

totalswaps=0
for i in range(0,len(a)):
    nbswaps=0
    for i in range(0,len(a)-1):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
            nbswaps+=1
    totalswaps+=nbswaps
    if nbswaps==0:
        break;
         
print("Array is sorted in",totalswaps,"swaps.")  
print("First Element:",str(a[0]))
print("Last Element:",str(a[-1]))
