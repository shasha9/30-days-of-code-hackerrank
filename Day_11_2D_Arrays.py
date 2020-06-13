#Given a 6x6 2D Array,A:
# hourglass in A is the subset of values with indices falling in this pattern in A's graphical representation and an hourglass sum is the sum of an hourglass' values.
#Task
#Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.


import sys


arr= []
sum=[]
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
for i in range(4):
    for j in range(4):
        num=arr[j][i]+arr[j][i+1]+arr[j][i+2]+arr[j+1][i+1]+arr[j+2][i]+arr[j+2][i+1]+arr[j+2][i+2]
        sum.append(num)
for i in range(15):
    if sum[i]>sum[i+1]:
        sum[i+1]=sum[i]
print(sum[15])
