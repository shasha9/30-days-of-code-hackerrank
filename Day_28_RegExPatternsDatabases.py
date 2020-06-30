#Task
#Consider a database table, Emails,
#which has the attributes First Name and Email ID. Given N rows of data simulating the Emails table, print an alphabetically-ordered list of people whose email address ends in @gmail.com .


import sys,re

names = []
pattern = re.compile('@gmail.com$')

N = int(input().strip())
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    if pattern.search(emailID):
        names.append(firstName)
import sys, re

names = []
pattern = re.compile('@gmail.com$')

N = int(input().strip())
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    if pattern.search(emailID):
        names.append(firstName)
names.sort()
for name in names:
    print(name)
