class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def showName(self):
        print(self.name)
    def showAge(self):
        print(self.age)
class Student:
    def __init__(self,studentId):
        self.studentId=studentId
    def getId(self):
        return self.studentId
class Resident(Person,Student):
    def __init__(self,name,age,id):
        Person.__init__(self,name,age)
        Student.__init__(self,id)

resident1=Resident('ABC',55,102)
resident1.showName()
print(resident1.getId())
