from Domain.Student import Student
from Domain.Exceptions import StudentException

class StudentRepository:
    def __init__(self):
        '''
        creates an instance of the StudentRepository
        '''
        self.__data = []
        
    def __find(self, ID):
        '''
        returns the index Student having the given ID
        Input: ID - positive integer, the ID of the Student that is being searched for
        Output: index - if the Student was found, -1 - otherwise 
        '''
        for i in range(len(self.__data)):
            if self.__data[i].getID() == ID:
                return i
        return -1
        
    def findByID(self, ID):
        '''
        returns the Student having the given ID
        Input: ID - positive integer, the ID of the Student that is being searched for
        Output: the Student, if found or None otherwise
        '''
        indexID = self.__find(ID) 
        if indexID == -1:
            return None
        return self.__data[indexID]
    
    def add(self, stu):
        '''
        adds a Student to the repository
        Input: stu - object of type Student
        Output: the given Student is added to the repository, if no other medicine with the same ID exists
        Exceptions: raises StudentException if another Student with the same ID already exists
        '''
        if self.findByID(stu.getID()) != None:
            raise StudentException("Student with ID " + str(stu.getID()) + " already exists!")
        self.__data.append(stu)
    
    def update(self, ID, newName):
        '''
        updates a Student from the repository, using its ID
        Input: ID - positive integer, the ID of the Student that must be updated
               newName - string, updated name of the Student
        Output: if such a Student exists, it is updated
        Exceptions: raises StudentException if a Student with the given ID does not exist
        '''
        indexID = self.__find(ID)
        if indexID == -1:
            raise StudentException("The is no Student with ID " + str(ID) + "!")
        self.__data[indexID].setName(newName)
            
    def remove(self, ID):
        '''
        removes a Student from the repository, using its ID
        Input: ID - positive integer, the ID of the Student that must be removed
        Output: if such a Student exists, it is removed and returned
        Exceptions: raises StudentException if a Student with the given ID does not exist
        '''
        indexID = self.__find(ID)
        if indexID == -1:
            raise StudentException("The is no Student with ID " + str(ID) + "!")
        self.__data.pop(indexID)
        
    def __len__(self):
        '''
        returns the size of the list of students
        '''
        return len(self.__data)
    
    def getAll(self):
        '''
        returns the list of students
        '''
        return self.__data

def testStudentRepository():
    repo = StudentRepository()
    
    s1 = Student(1, "Vasilica")
    s2 = Student(1, "Gheorghidiu")
    
    assert len(repo) == 0
    
    repo.add(s1)
    assert len(repo) == 1
    assert repo.findByID(1) == s1
    
    try:
        repo.add(s1)
        assert False
    except StudentException:
        assert True
        
    try:
        repo.add(s2)
        assert False
    except StudentException:
        assert True
        
    s2 = Student(2, "Gheorghidiu")
    repo.add(s2)
    assert len(repo) == 2
    assert repo.findByID(1) == s1
    assert repo.findByID(2) == s2
    
    repo.update(2,"Johnny Bravo")
    
    assert len(repo) == 2
    repo.remove(1)
    assert len(repo) == 1
    assert repo.findByID(2) == s2
    assert repo.findByID(1) == None
    
    try:
        repo.remove(1)
        assert False
    except StudentException:
        assert True
    
    repo.remove(2)
    assert len(repo) == 0
    
if __name__ == '__main__':
    testStudentRepository()
