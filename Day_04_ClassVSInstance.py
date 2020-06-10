#Task
# Write a person class with an instance variable age and a constructor that takes an integer initialAge as a parameter. 
#The constructor must assign initialAge to age after confirming the argument past as initialAge is not negative;
#if a negative argument is passed past as initilAge, the constructor should set age 20 to 0 and print "age is not valid setting age to 0"
#In addition you must write the following instance methods: 
#yearPasses() should increase the age instance variable by 1
#amIOld() should perform the following conditional actions:
#if age<13 print "you are young"
#if age<=13 and age<18 print "you are a teenager" otherwise print "you are old".

class Person:
    age=0
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge < 0:
            print ("Age is not valid, setting age to 0.")
        else:
            self.age= initialAge
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age < 13:
            print ("You are young.")
        elif self.age >= 13 and self.age < 18:
            print ("You are a teenager.")
        else:
            print ("You are old.")
    def yearPasses(self):
        # Increment the age of the person in here
        self.age=self.age+ 1
