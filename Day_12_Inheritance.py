#Task
#Given two classes, Person and Student, where Person is the base class and Student is the derived class. 
#Student inherits all the properties of Person.

class Student(Person):
    def __init__(self,firstHame,lastName,idNumber,scores):
        Person.__init__(self,firstHame,lastName,idNumber)
        self.scores=scores
    def calculate(self):
        sum=0
        n=0
        for i in range(len(self.scores)):
            sum=sum+int(self.scores[i])
            n=n+1
        sum=sum//n
        if sum>=90 and sum<=100:
            return 'O'
        elif sum>=80 and sum<90:
            return 'E'
        elif sum>=70 and sum<80:
            return 'A'
        elif sum>=55 and sum<70:
            return 'P'
        elif sum>=40 and sum<55:
            return 'D'
        else:
            return 'T'
