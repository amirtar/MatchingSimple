
#Author: Ali Mirtar, PhD.

#Date: Jan/29/2018

#Contact: amirtar@alumni.ucsd.edu

#Use under GNU GPL3 license

#### core simulation

class Student:
    count = 0
    def __init__(self, name):
        self.name = name
        self.rank = []
        self.match = None
        self.next =0
        Student.count += 1

    def getNext(self):
        if (self.next >= len(self.rank)):
            return None
        self.next += 1
        return self.rank[self.next-1]
        
    def addInstitute(self, institute):
        self.rank.append(institute)

    def addInstitutes(self, institutes):
        self.rank.extend(institutes)

    def resetRank(self):
        self.rank = []

    def printRank(self):
        output = ":".join([self.name, ",".join([i.name for i in self.rank])])
        return output
    
    def __str__(self):
        return self.printRank()
    def __repr__(self):
        return self.printRank()
        

class Institute:
    count = 0
    def __init__(self,name, positions = 0):
        self.name = name
        self.rank = []
        self.positions = 2
        self.accepted = []
        Institute.count += 1

    def match(self, student):
        if student not in self.rank:
            return student
        if len(self.accepted)<self.positions :
            self.accepted.append(student)
            return None
        studentRank = self.rank.index(student)
        maxAcceptedRank = -1
        rejectedStudent = None
        for acceptedStudent in self.accepted:
            acceptedRank = self.rank.index(acceptedStudent)
            if acceptedRank > maxAcceptedRank :
                maxAcceptedRank = acceptedRank
                rejectedStudent = acceptedStudent
        if studentRank < maxAcceptedRank:
            self.accepted.remove(rejectedStudent)
            self.accepted.append(student)
        else:
            rejectedStudent = student
        return rejectedStudent
        

    def addStudent(self, student):
        self.rank.append(student)

    def addStudents(self, students):
        self.rank.extend(students)

    def resetRank(self):
        self.rank=[]

    def printRank(self):
        output = ":".join([self.name, ",".join([s.name for s in self.rank])])
        return output

    def __str__(self):
        return self.printRank()
    def __repr__(self):
        return self.printRank()

class MatchingScenario:
    def __init__(self,name, students, institutes, info=""):
        self.name =name
        self.info =info
        self.students = students
        self.institutes = institutes
        self.solved = False

    def results(self):
        if not self.solved :
            return "Not Solved"
        output = []
        for student in self.students:
            if student.match == None:
                output.append(student.name +": No Match")
            else:
                output.append(student.name +":"+ student.match.name)
        return "\n".join(output)

    def __str__(self):
        output1 = ["Students:"]
        output1.extend(["\t"+str(s) for s in self.students])
        output2 = ["Institutes:"]
        output2.extend(["\t"+str(i) for i in self.institutes])
        return "\n".join([self.name, "Info: "+self.info, "\n".join(output1), "\n".join(output2)])

    def __repr__(self):
        return str(self)
        
class MatchingSolver:
    @classmethod
    def solve(cls, scenario):
        print(scenario)
        print("Solving...")
        while(not scenario.solved):
            scenario.solved = True
            for student in scenario.students:
                if student.match != None :
                    continue
                institute = student.getNext()
                if institute != None :
                    unmatchedStudent = institute.match(student)
                    if unmatchedStudent !=student :
                        scenario.solved = False
                        student.match = institute
                        if unmatchedStudent !=None :
                            unmatchedStudent.match = None
            
    

#### specific Scenarios

def createScenario1():
    mercy   = Institute("Mercy"   , 2)
    city    = Institute("City"    , 2)
    general = Institute("General" , 2)
    institutes = [mercy, city, general]
    
    arthur  = Student("Arthur")
    sunny   = Student("Sunny")
    joseph  = Student("Joseph")
    latha   = Student("Latha")
    darrius = Student("Darrius")
    students = [arthur, sunny, joseph, latha, darrius]
    
    scenario1 = MatchingScenario("nrmp Scenario",students, institutes, "https://youtu.be/kvgfgGmemdA")
    
    arthur.addInstitute(city)
    sunny.addInstitutes([city, mercy])
    joseph.addInstitutes([city, general, mercy])
    latha.addInstitutes([mercy, city, general])
    darrius.addInstitutes([city, mercy, general])

    mercy.addStudents([darrius, joseph])
    city.addStudents([darrius, arthur, sunny, latha, joseph])
    general.addStudents([darrius, arthur, joseph, latha])

    return scenario1
    

if (__name__== "__main__"):

    scenario1 = createScenario1()
    MatchingSolver.solve(scenario1)
    print(scenario1.results())
