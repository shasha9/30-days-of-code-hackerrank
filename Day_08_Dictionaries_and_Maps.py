#Task
#Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. 
#You will then be given an unknown number of names to query your phone book for. For each name queried, 
#print the associated entry from your phone book on a new line in the form name=phoneNumber; 
#if an entry for name is not found, print Not found instead.

N = int(input())
phone_book = {}

for i in range(N):
    a = input().split()
    phone_book[a[0]] = a[1]
  
for j in range(N):
    b = str(input())
    if b not in phone_book:
        print ("Not found")
    else:
        print (str(b) + "=" + str(phone_book[b]))
