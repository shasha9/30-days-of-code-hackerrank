#Task
#Given a string, S , of length N that is indexed from 0 to N-1, 
#print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line.

if __name__ == '__main__':

    test = int(input())
    for i in range(test):
        s = input()
        
        for i in range (len(s)):
            if i%2 == 0:
                print(s[i],sep = "", end = "")
        
        print(" ",sep = "", end = "")

        for i in range (len(s)):
            if i%2 == 1:
                print(s[i],sep = "", end = "")
        
        print("")
