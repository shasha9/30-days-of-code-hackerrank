#Task
#Take each character in s , enqueue it in a queue, and also push that same character onto a stack. 
#Once that's done,dequeue the first character from the queue and pop the top character off the stack, then compare the two characters to see if they are the same; 
#as long as the characters match, 
#we continue dequeueing, popping, and comparing each character until containers are empty (a non-match means s isn't a palindrome).

import sys

class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []

    def popCharacter(self):
        return self.stack.pop()

    def pushCharacter(self, char):
        self.stack.append(char)

    def dequeueCharacter(self):
        char = self.queue[0]
        self.queue = self.queue[1:]
        return char

    def enqueueCharacter(self, char):
        self.queue.append(char)

s=input()

obj=Solution()   

l=len(s)
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break

if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    
     
    
