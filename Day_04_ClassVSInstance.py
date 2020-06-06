#Task
# Write a person class with an instance variable age and a constructor that takes an integer initiated as a parameter the constructor much to sign initial age to age after confirming the argument past as initial age is not negative past as initially is the constructor should set age 20 and print age is not valid setting age to 0 in addition you must write the following instance methods year passes should increase the age instance variable-I am I also perform the following condition elections if it is less than 13 print you are young age is greater than equal to 13 and you just listen 18 print you are a teenager otherwise friend you are old





class Person:
    age=0
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge < 0:
            print ("Age is not valid, setting age to 0.")
        else:
            self.age = initialAge
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
