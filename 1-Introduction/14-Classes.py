###
student = {"name": "Rolf", "grades": (89,90,93,78,90)}

def average(sequence):
    return sum(sequence)/ len(sequence)

###print(average(student['grades']))
###

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grades = grade

    def average(self):
        return(sum(self.grades)/len(self.grades))

student = Student("Bob", (100,200,300))
print(student.name)
print(student.average())