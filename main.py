from objects import *
courseList = [k.name for k in Course.numReg]

def main():
    print('Welcome to the virtual university!')
    studentOrProfessor()

# It will show [1]Student  [2]Professor  [3]Students of particular course
def studentOrProfessor():
    print('1) Student   2) Professor     3) see the courses')
    # noinspection PyBroadException
    try:
        answer = int(input())
    except:
        print('Choose a number from the given options above.!')
        studentOrProfessor()
    if answer == 1:
        studentNumber()
    elif answer == 2:
        professorID()
    elif answer == 3:
        seeTheCourses()
    else:
        print('Choose a number from the given options above.!')
        studentOrProfessor()

# Input for Student Number
def studentNumber():
    print('Enter you University Student Number: ')
    global numStudent
    numStudent = int(input())
    #Please start the roll number from 101, since it is technically not possible for me to include a large list starting from 1.
    lenOfStudents =  100 + len(Student.numReg) + 1 
    if numStudent in range(101, lenOfStudents):
        studentAuth()
    else:
        print('Wrong Student Number Inputted!')
        studentNumber()

# Display the details of the student
def studentAuth():
    for i in Student.numReg:
        if i.number == numStudent:
            i.displayStudent()
    studentMenu()

# It will show [1]See your courses [2]Join a new course [3]Log out
def studentMenu():
    print('1) See your courses   2) Join a new course    3) Log out')
    userOption = int(input())
    if userOption == 1:
        seeStudentCourses()
    elif userOption == 2:
        getNewCourse()
    elif userOption == 3:
        studentOrProfessor()
    else:
        print('Please choose a valid option from the student menu')
        studentMenu()

# This is used to list the number of courses a student has taken
def seeStudentCourses():
    for i in Student.numReg:
        i.displayStudentCourses(numStudent)
    studentMenu()

# This is used to select a new course
def getNewCourse():
    print('Select the course you want to attend : ')
    for k in Course.numReg:
        k.displayCourses()
    selectedCourseNumber = int(input())
    if selectedCourseNumber in range(1, len(Course.numReg)+1):
        wantedCourse = courseList[selectedCourseNumber - 1]
        for i in Student.numReg:
            i.studentCourseAdding(wantedCourse, numStudent)
        for k in Course.numReg:
            k.newStudentGotACourse(numStudent, wantedCourse)
        studentMenu()
    else:
        print('Choose a valid number for given course')
        getNewCourse()

# This is used to check the Professor's ID number
def professorID():
    print('Your ID?')
    global numProfessor
    numProfessor = int(input())
    if numProfessor in range(1, len(Professor.numReg)+1):
        professorAuth()
    else:
        print('Please type a valid professor ID!')
        professorID()

# This is used to check the Professor's details
def professorAuth():
    for j in Professor.numReg:
        j.displayProfessor(numProfessor)
    professorMenu()

# It will show [1]List of attending students [2]Create a new course [3]Log out
def professorMenu():
    print('1) List of attending students   2) Create a new course   3) Log out')
    professorOption = int(input())
    if professorOption == 1:
        for j in Professor.numReg:
            if j.number == numProfessor:
                if len(j.profCourses) == 0:
                    print('You have not given any courses!!')
                    professorMenu()
                else:
                    whichCourseToSee()
    elif professorOption == 2:
        profGiveNewCourse()
    elif professorOption == 3:
        studentOrProfessor()
    else:
        print('Invalid option selected. Please choose a valid choice.')
        professorMenu()

# The Professor is able to see the number of students attending the particular chosen course
def whichCourseToSee():
    print('Type the name of the course to list whether the student is enrolled : ')
    for j in Professor.numReg:
        if j.number == numProfessor:
            for l in range(0, len(j.profCourses)):
                print('%d. %s' % (l + 1, j.profCourses[l]))

            courseSelectionToSeeStudents = int(input())

            if 1 <= courseSelectionToSeeStudents <= len(j.profCourses):
                studentCount = 1
                courseName = j.profCourses[courseSelectionToSeeStudents - 1]
                for i in Student.numReg:
                    for z in range(0, len(i.courses)):
                        if i.courses[z] == courseName:
                            print('%d. ' % studentCount + i.name + ' ' + i.family)
                            studentCount += 1
                        else:
                            pass

                if studentCount == 1:
                    print('No students have selected this course')

                professorMenu()

            else:
                print('Invalid course number selected.')
                whichCourseToSee()

# The professor can allot a new course
def profGiveNewCourse():
    print('Write the name of the course :')
    for k in Course.numReg:
        k.displayCourses()
    newCourseOption = int(input())
    if newCourseOption in range(1, len(Course.numReg)+1):
        Professor.professorCourseGiving(newCourseOption, numProfessor)
        professorMenu()
    else:
        print('Invalid course number selected.')
        profGiveNewCourse()

# the user selected to see the course details (option 3 in main menu)
def seeTheCourses():
    print('Which course to see the details of?')
    for k in Course.numReg:
        k.displayCourses()
    courseNumber = int(input())
    if courseNumber in range(1, len(Course.numReg)+1):
        for k in Course.numReg:
            k.displayCourseDetails(courseNumber)
        studentOrProfessor()
    else:
        print('please type a valid course number!')
        seeTheCourses()

if __name__ == '__main__':
    main()
from objects import *
courseList = [k.name for k in Course.numReg]

def main():
    print('Welcome to the virtual university!')
    studentOrProfessor()

# It will show [1]Student name [2]Professor name [3]Students of particular course
def studentOrProfessor():
    print('1) Student name   2) Professor name    3) see the courses')
    # noinspection PyBroadException
    try:
        answer = int(input())
    except:
        print('Choose a number from the given options above.!')
        studentOrProfessor()
    if answer == 1:
        studentNumber()
    elif answer == 2:
        professorID()
    elif answer == 3:
        seeTheCourses()
    else:
        print('Choose a number from the given options above.!')
        studentOrProfessor()

# Input for Student Number
def studentNumber():
    print('Enter you University Student Number: ')
    global numStudent
    numStudent = int(input())
    lenOfStudents =  9700 + len(Student.numReg) + 1 # student numbers are start from 9701
    if numStudent in range(9701, lenOfStudents):
        studentAuth()
    else:
        print('Wrong Student Number Inputted!')
        studentNumber()

# Display the details of the student
def studentAuth():
    for i in Student.numReg:
        if i.number == numStudent:
            i.displayStudent()
    studentMenu()

# It will show [1]See your courses [2]Join a new course [3]Log out
def studentMenu():
    print('1) See your courses   2) Join a new course    3) Log out')
    userOption = int(input())
    if userOption == 1:
        seeStudentCourses()
    elif userOption == 2:
        getNewCourse()
    elif userOption == 3:
        studentOrProfessor()
    else:
        print('Please choose a valid option from the student menu')
        studentMenu()

# This is used to list the number of courses a student has taken
def seeStudentCourses():
    for i in Student.numReg:
        i.displayStudentCourses(numStudent)
    studentMenu()

# This is used to select a new course
def getNewCourse():
    print('Select the course you want to attend : ')
    for k in Course.numReg:
        k.displayCourses()
    selectedCourseNumber = int(input())
    if selectedCourseNumber in range(1, len(Course.numReg)+1):
        wantedCourse = courseList[selectedCourseNumber - 1]
        for i in Student.numReg:
            i.studentCourseAdding(wantedCourse, numStudent)
        for k in Course.numReg:
            k.newStudentGotACourse(numStudent, wantedCourse)
        studentMenu()
    else:
        print('Choose a valid number for given course')
        getNewCourse()

# This is used to check the Professor's ID number
def professorID():
    print('Your ID?')
    global numProfessor
    numProfessor = int(input())
    if numProfessor in range(1, len(Professor.numReg)+1):
        professorAuth()
    else:
        print('Please type a valid professor ID!')
        professorID()

# This is used to check the Professor's details
def professorAuth():
    for j in Professor.numReg:
        j.displayProfessor(numProfessor)
    professorMenu()

# It will show [1]List of attending students [2]Create a new course [3]Log out
def professorMenu():
    print('1) List of attending students   2) Create a new course   3) Log out')
    professorOption = int(input())
    if professorOption == 1:
        for j in Professor.numReg:
            if j.number == numProfessor:
                if len(j.profCourses) == 0:
                    print('You have not given any courses!!')
                    professorMenu()
                else:
                    whichCourseToSee()
    elif professorOption == 2:
        profGiveNewCourse()
    elif professorOption == 3:
        studentOrProfessor()
    else:
        print('Invalid option selected. Please choose a valid choice.')
        professorMenu()

# The Professor is able to see the number of students attending the particular chosen course
def whichCourseToSee():
    print('Type the name of the course to list the student attendance : ')
    for j in Professor.numReg:
        if j.number == numProfessor:
            for l in range(0, len(j.profCourses)):
                print('%d. %s' % (l + 1, j.profCourses[l]))

            courseSelectionToSeeStudents = int(input())

            if 1 <= courseSelectionToSeeStudents <= len(j.profCourses):
                studentCount = 1
                courseName = j.profCourses[courseSelectionToSeeStudents - 1]
                for i in Student.numReg:
                    for z in range(0, len(i.courses)):
                        if i.courses[z] == courseName:
                            print('%d. ' % studentCount + i.name + ' ' + i.family)
                            studentCount += 1
                        else:
                            pass

                if studentCount == 1:
                    print('No students have selected this course')

                professorMenu()

            else:
                print('Invalid course number selected.')
                whichCourseToSee()

# The professor can allot a new course
def profGiveNewCourse():
    print('Write the name of the course :')
    for k in Course.numReg:
        k.displayCourses()
    newCourseOption = int(input())
    if newCourseOption in range(1, len(Course.numReg)+1):
        Professor.professorCourseGiving(newCourseOption, numProfessor)
        professorMenu()
    else:
        print('Invalid course number selected.')
        profGiveNewCourse()

# the user selected to see the course details (option 3 in main menu)
def seeTheCourses():
    print('Which course to see the details of?')
    for k in Course.numReg:
        k.displayCourses()
    courseNumber = int(input())
    if courseNumber in range(1, len(Course.numReg)+1):
        for k in Course.numReg:
            k.displayCourseDetails(courseNumber)
        studentOrProfessor()
    else:
        print('please type a valid course number!')
        seeTheCourses()

if __name__ == '__main__':
    main()
