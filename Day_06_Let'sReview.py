#Task
#Given a string, S , of length N that is indexed from 0 to N-1, 
#print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line.

n = int(input())

for i in range(0, n):
 string = input()
 print(string[::2],string[1::2])

