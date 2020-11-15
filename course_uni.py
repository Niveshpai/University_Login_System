from student import Student

class Course:
    # Using a global base for all the available courses
    numReg = []

    # We will initalise the course class
    def __init__(self, number, name, Course_Professor=None, Student_attempting_course=None):
        if Student_attempting_course is None:
            Student_attempting_course = []
        self.number = number
        self.name = name
        self.Course_Professor = Course_Professor
        self.Student_attempting_course = Student_attempting_course
        self.numReg.append(self)

    # To display name and the number of the course
    def displayCourses(self):
        print('%d) %s' % (self.number, self.name))

    # It will show [1]Student name [2]Professor name [3]Students of particular course
    def displayCourseDetails(self, courseNumber):
        if self.number == courseNumber:
            print('Course name : ' + self.name)
            if self.Course_Professor:
                print('Professor name :  ' + self.Course_Professor)
            else:
                print('No professor has chosen this particular course to teach!')

            if len(self.Student_attempting_course) > 0:
                print('The number of attending student/s are: ' + str([self.Student_attempting_course[q] for q in range(0, len(self.Student_attempting_course))]))
            else:
                print('No students have taken up the course.')

    # It is used to add the details of the students registering for the first time to the overall course list
    def Student_with_new_course(self, numStudent, wantedCourse):
        if wantedCourse == self.name:
            for i in Student.numReg:
                if numStudent == i.number:
                    nameAndFamily = i.name + ' ' + i.family
                    self.Student_attempting_course.append(nameAndFamily)