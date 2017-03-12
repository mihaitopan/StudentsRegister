class Grade:
    def __init__(self, discipline, studentID, grade):
        '''
        creates a new instance of Grade
        '''
        self.__discipline = discipline
        self.__studentID = studentID
        self.__grade = grade
        
    def getDiscipline(self):
        '''
        getter for the disciplines name
        '''
        return self.__discipline
    
    def setDiscipline(self, discipline):
        '''
        setter for the disciplines name
        '''
        self.__discipline = discipline
        
    def getStudentID(self):
        '''
        getter for the Student's ID
        '''
        return self.__studentID
    
    def setStudentID(self, studentID):
        '''
        setter for the Student's ID
        '''
        self.__studentID = studentID
        
    def getGrade(self):
        '''
        getter for the grade
        '''
        return self.__grade
    
    def setGrade(self, grade):
        '''
        setter for the grade
        '''
        self.__grade = grade
        
    def __eq__(self, other):
        return type(self) == type(other) and \
                self.getDiscipline() == other.getDiscipline() and \
                self.getStudentID() == other.getStudentID() and \
                self.getGrade() == other.getGrade()
        
    def __str__(self):
        return "DISCIPLINE: " + self.__discipline + "\t STUDENT ID: " + str(self.__studentID) + "\t GRADE: " + str(self.__grade)
        
def testGrade():
    gra = Grade("maths", 1, 8)
    assert gra.getDiscipline() == "maths"
    assert gra.getStudentID() == 1
    assert gra.getGrade() == 8
    gra.setDiscipline("physics")
    gra.setStudentID(2)
    gra.setGrade(9)
    assert gra.getDiscipline() == "physics"
    assert gra.getStudentID() == 2
    assert gra.getGrade() == 9

if __name__ == '__main__':
    testGrade()
