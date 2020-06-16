#Complete the Difference class by writing the following:

#A class constructor that takes an array of integers as a parameter and saves it to the elements instance variable.
#A computeDifference method that finds the maximum absolute difference between any 2 numbers in N and stores it in the maximumDifference instance variable.

   def computeDifference(self):
        self.maximumDifference= 0
        for x in range(len(a)):
            for y in range(x,len(a)):
                if abs(a[x] - a[y]) > self.maximumDifference:
                    self.maximumDifference = abs(a[x] - a[y])
