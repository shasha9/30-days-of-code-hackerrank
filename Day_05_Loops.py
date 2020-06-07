#Task
#Given an integer,n, print its first 10 multiples. 
#Each multiple nxi  (where 1<=i<=10 )should be printed on a new line in the form: n x i = result.

#!/bin/python3

import sys


N = int(input().strip())
for i in range(1,11):
    print(str(N) + " x " + str(i) + " = " + str(N*i))
