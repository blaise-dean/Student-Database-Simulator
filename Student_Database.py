import random
import json

#lists
coursesList = ['English 1', 'English 2', 'Algebra 1', 'Algebra 2', 'Calculus 1', 'Calculus 2',
            'Art', 'Spanish', 'Computer Science', 'Engineering', 'Pre-Medical', 'History',
            'Spanish 2'
           ]

studentData = []

studentList = []

#blueprint for creating a student
class Student:
    def __init__(self, GPA: float, courses: list, ID: int, name: str):
        self.GPA = GPA
        self.courses = courses
        self.ID = ID
        self.name = name

    def checkCourse(self):
        print(self.courses)

    def checkGPA(self):
        print(self.GPA)
    
    def checkID(self):
        print(self.ID)

    def searchStudent(self,search):
        if search == self.name:
            check = input("What would you like to check?\n1.GPA\n2.courses\n3.ID\n")
            if check == '1' or check == 'GPA':
                print(f'{self.name} GPA is {self.GPA}')
            elif check == '2' or check == 'courses':
                print(self.courses)
            elif check == '3' or check == 'ID':
                print({self.ID})
            else:
                print("Invalid Input.")
            

#Main Loop
while True:
    
    #student user creation
    prompt = input("Would you like to:\n1. Create a student\n2. Search a student\n3. Update student GPA\n4. Remove a student\n5. List students\n6. Load data\n7. Save and exit\n").lower()
    if prompt == '1':

        studentName = input("What is the students name? ")

        #Check if user already in database
        for student in studentList:
            while studentName == student.name:
                studentName = input("Student already in database, try again. ")

        studentGPA = float(input("What is the users gpa? "))
        studentID = int(input("What is the students ID? "))

        if studentName == any(studentList):
            while studentName == any(studentList):
                studentName = input("Name is taken. Try again: ")

        studentCourses = []

        studentCourses.append(random.sample(coursesList, 6))

        #Creates student instance
        student = Student(studentGPA, studentCourses, studentID, studentName)

        studentList.append(student)
    
    #student search
    elif prompt == '2':
        search = input("What student would you like to search? ")
        for students in studentList:
            students.searchStudent(search)
    
    #student update
    elif prompt == '3':
        updateStudent = input("Which student would you like to update? ")
        for student in studentList:
            if updateStudent == student.name:
                newGPA = float(input("What should the students new GPA be? "))
                student.GPA = newGPA
                print(student.name + "'s new gpa is " + str(student.GPA))
                

    #student remove
    elif prompt == '4':
        removeStudent = input("Which student would you like to remove? name/ID ")
        print('')
        for students in studentList:
            if removeStudent == str(student.ID) or removeStudent == student.name:
                studentList.remove(student)
                print(f"{student.name} has been removed.")
            else:
                print("Student does not exist.")
                continue

    #show list
    elif prompt == '5':
        for student in studentList:
            print(student.name)
    
    #load data
    elif prompt == '6':
        with open('Save.json', 'r') as file:
            loadData = json.load(file)
        for s in loadData:
                studentList.append(Student(s['GPA'], s['courses'], s['ID'], s['name']))
                print("Student data has been loaded!")

    #break
    elif prompt == '7':
        break

    #else
    else:
        print("Invalid input")

#adds student data to the list
for student in studentList:
    studentData.append({
    "name": student.name,
    "GPA": student.GPA,
    "ID": student.ID,
    "courses": student.courses
    })


#writes data to file
with open('Save.json', 'w') as file:
    json.dump(studentData, file, indent = 4)
        
    

