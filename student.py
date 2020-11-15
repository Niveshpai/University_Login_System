class Student:
    # Using a global base for all the available courses
    numReg = []

    # We will initalise the student class
    def __init__(self, number, name, family, courses=None):
        if courses is None:
            courses = []
        self.number = number
        self.numReg.append(self)
        self.name = name
        self.family = family
        self.courses = courses

    # This is used to display the student details
    def displayStudent(self):
        print('You are logged in as ' + self.name + ' ' + self.family)

    # This is used to display the number of courses a student takes up during his term/semester
    def displayStudentCourses(self, numStudent):
        if self.number == numStudent:
            if self.courses:
                print(self.courses)
            else:
                print('You have not selected any courses. Please choose a course.')

    # Using this, the selected course will be added to the student's portfolio/data
    def studentCourseAdding(self, wantedCourse, numStudent):
        if self.number == numStudent:
            self.courses.append(wantedCourse)
            print('You Added ' + wantedCourse + ' to your schedule, successfully!')