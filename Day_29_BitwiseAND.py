#Task
#Given set S={1,2,3,...N}.Find two integers,A and B(where A<B)
#from set S such that the value of A and B is the maximum possible and also less than a given integer,K.In this case,& represents the bitwise AND operator.

import sys
import math

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    
    
    if (k-2)&(k-1)==(k-1):
        print(k-1)
    else:
        maxab=0
        a=min(n,2**int(math.log(k,2)+1))
        while a>maxab:
            for b in range(maxab, a):
                if a&b<k:
                    maxab=max(maxab,a&b)
            a-=1
        print(maxab)
        
        '''
        for a in range(1,n):
            for b in range(a+1,min(n,2**(int(math.log(a,2))+2)+1)):
                if a&b<k:
                    maxab=max(maxab,a&b)
        print(maxab)
