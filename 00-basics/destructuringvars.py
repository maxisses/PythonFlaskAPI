## tuple, no klammern required
x = 5, 11

## list with tuple inside
y = [(5,11)]

## 2 vars
x, y = 5, 11

print(f"{x} ist the value of x")


student_attendance = {"Max": 55, "Lilli": 53}#

print(student_attendance.items())

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")


person = ("Ralf", 45, "Mechanic")

## _ variable is meant to be ignored; convention
name, _, profession = person
print(name, profession)

## puts all values in second var, except the first value of the list
head, *tail = [1,2,3,4,5]
print(head)
print(tail)