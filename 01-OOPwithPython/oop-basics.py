student = {"name": "Rolf", "grades": (89,90,93,78,90)}


def average(sequence):
    return sum(sequence) / len(sequence)

print(average(student["grades"]))

class Student:
    ##inside a class functions are called methods
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    
    def average(self):
        return sum(self.grades) / len(self.grades)


student1 = Student("Bob", (20,15,16,17))

print(student1.name)
print(student1.average())


student2 = Student("Max", (15,15,16,17))

print(student2.name)
print(student2.average())