#Task
#Write a Calculator class with a single method: int power(int,int). 
#The power method takes two integers, n and p, as parameters and returns the integer result of n to the power p.
#If either n or p is negative,then the method must throw an exception with the message: n and p should be non-negative.

class Calculator:
    def power(self,n,p):
        if n>=0 and p>=0:
            return pow(n,p)
        else:
            raise Exception('n and p should be non-negative')
