from Domain.Grade import Grade
from Domain.Exceptions import GradeException

class GradeRepository:
    def __init__(self):
        '''
        creates an instance of the GradeRepository
        '''
        self.__data = []
    
    def __findDis(self, discipline):
        '''
        returns the index Grade having the given discipline
        Input: discipline - string, the discipline of the Grade that is being searched for
        Output: index - if the Grade was found, -1 - otherwise 
        '''
        for i in range(len(self.__data)):
            if self.__data[i].getDiscipline() == discipline:
                return i
        return -1
    
    def findByDiscipline(self, discipline):
        '''
        returns the Grade having the given discipline
        Input: discipline - string, the discipline of the Grade that is being searched for
        Output: the Grade, if found or None otherwise
        '''
        indexDiscipline = self.__findDis(discipline) 
        if indexDiscipline == -1:
            return None
        return self.__data[indexDiscipline]
    
    def __findStu(self, studentID):
        '''
        returns the index Grade having the given studentID
        Input: studentID - positive integer, the studentID of the Grade that is being searched for
        Output: index - if the Grade was found, -1 - otherwise 
        '''
        for i in range(len(self.__data)):
            if self.__data[i].getStudentID() == studentID:
                return i
        return -1
    
    def findByStudentID(self, studentID):
        '''
        returns the Grade having the given studentID
        Input: studentID - positive integer, the studentID of the Grade that is being searched for
        Output: the Grade, if found or None otherwise
        '''
        indexStudentID = self.__findStu(studentID) 
        if indexStudentID == -1:
            return None
        return self.__data[indexStudentID]
    
    def __find(self, discipline, studentID):
        '''
        returns the index Grade having the given discipline and studentID
        Input: studentID - positive integer, the studentID of the Grade that is being searched for
               discipline - string, the discipline of the Grade that is being searched for
        Output: index - if the Grade was found, -1 - otherwise 
        '''
        for i in range(len(self.__data)):
            if self.__data[i].getDiscipline() == discipline and self.__data[i].getStudentID() == studentID:
                return i
        return -1
        
    def findByDisciplineAndStudentID(self, discipline, studentID):
        '''
        returns the Grade having the given discipline and studentID
        Input: studentID - positive integer, the studentID of the Grade that is being searched for
               discipline - string, the discipline of the Grade that is being searched for
        Output: the Grade, if found or None otherwise
        '''
        indexDisciplineAndStudentID = self.__find(discipline, studentID) 
        if indexDisciplineAndStudentID == -1:
            return None
        return self.__data[indexDisciplineAndStudentID]
    
    def addStudentToDiscipline(self, discipline, studentID):
        '''
        adds a student to a discipline
        Input: discipline - string, the name of the discipline that the student must be added to
               studentID - positive integer, the ID of the student to add to the discipline
        Output: the given Grade is added to the repository, if no other Grade with the same discipline and studentID exists
                ! the given Grade's grade is initialized with 0
        Exceptions: raises GradeException if another Grade with the same discipline and studentID already exists
        '''
        if self.findByDisciplineAndStudentID(discipline, studentID) != None:
            raise GradeException("Student with ID " + str(studentID) + " already added to discipline " + discipline + "!")
        gra = Grade(discipline, studentID, 0)
        self.__data.append(gra)
        
    def updateGrade(self, discipline, studentID, grade):
        '''
        updates a Grade's grade
        Input: discipline - string, the name of the discipline that the student must be added to
               studentID - positive integer, the ID of the student to add to a discipline
               grade - float, 1<= grade <= 10, the grade to be updated
        Output: if such a Grade exists, it is updated
        Exceptions: raises GradeException if a Grade with the given discipline and studentID does not exist
        '''
        indexGrade = self.__find(discipline, studentID)
        if indexGrade == -1:
            raise GradeException("Student with ID " + str(self.__data[indexGrade].getStudentID()) + " must be added first to discipline " + self.__data[indexGrade].getDiscipline() + "!")
        self.__data[indexGrade].setGrade(grade)
        
    def removeStudentFromDiscipline(self, discipline, studentID):
        '''
        removes a student from a discipline
        Input: discipline - string, the name of the discipline that the student must be removed from
               studentID - positive integer, the ID of the student to remove from the discipline
        Output: if such a Grade exists, it is removed and returned
        Exceptions: raises GradeException if a Grade with the given discipline and studentID does not exist
        '''
        indexDisciplineAndStudentID = self.__find(discipline, studentID)
        if indexDisciplineAndStudentID == -1:
            raise GradeException("There is no student with the ID: " + str(studentID) + " added to discipline: " + discipline + "!")
        self.__data.pop(indexDisciplineAndStudentID)
        
    def __len__(self):
        '''
        returns the size of the list of grades
        '''
        return len(self.__data)
    
    def getAll(self):
        '''
        returns the list of grades
        '''
        return self.__data
    
def testGradeRepository():
    repo = GradeRepository()
    
    assert len(repo) == 0
    
    repo.addStudentToDiscipline("maths", 1)
        
    assert len(repo) == 1
    g1 = Grade("maths", 1, 0)

    assert repo.findByDisciplineAndStudentID("maths", 1) == g1

    try:
        repo.addStudentToDiscipline("maths", 1)
        assert False
    except GradeException:
        assert True
        
    try:
        repo.updateGrade("maths", 8, 10)
        assert False
    except GradeException:
        assert True
     
    repo.updateGrade("maths", 1, 10)
    assert len(repo) == 1
    
    g2 = Grade("maths", 1, 10)
    assert repo.findByDisciplineAndStudentID("maths", 1) == g2

    repo.removeStudentFromDiscipline("maths", 1)
    assert len(repo) == 0
    
    try:
        repo.removeStudentFromDiscipline("maths", 1)
        assert False
    except GradeException:
        assert True

if __name__ == '__main__':
    testGradeRepository()
