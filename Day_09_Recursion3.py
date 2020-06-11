#Task
#Write a factorial function that takes a positive integer,N as a parameter and prints the result of N! (factorial).

def factorial(n): 
      
   return 1 if (n==1 or n==0) else n * factorial(n - 1)
  

num =int(input())
print( factorial(num)) 
