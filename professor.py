from course_uni import Course

class Professor:
    # Global declaration of base class
    numReg = []

    # Initialize course class
    def __init__(self, number, family, profCourses=None):
        if profCourses is None:
            profCourses = []
        self.number = number
        self.numReg.append(self)
        self.family = family
        self.profCourses = profCourses

    # Welcome message for respective professor and details of particular courses
    def displayProfessor(self, numProfessor):
        if self.number == numProfessor:
            print('Welcome  Dr.' + self.family)
            print('You are the instructor of %d course(s) ' % len(self.profCourses))

    # On selecting appropriate option, a new course will be added to the professor's list.
    @staticmethod
    def professorCourseGiving(newCourseOption, numProfessor):
        for k in Course.numReg:
            if k.number == newCourseOption:
                courseProf = k.profOfCourse
        if courseProf:
            print('Sorry Sir! Another professor has instructed this course, before!')
        else:
            for k in Course.numReg:
                if k.number == newCourseOption:
                    for j in Professor.numReg:
                        if j.number == numProfessor:
                            j.profCourses.append(k.name)
                            k.profOfCourse = j.family
            courseList = [k.name for k in Course.numReg]
            print('You are now the instructor of %s!' % courseList[newCourseOption-1])
