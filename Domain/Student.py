class Student:
    def __init__(self, ID, name):
        '''
        creates a new instance of Student
        '''
        self.__ID = ID
        self.__name = name
    
    def getID(self):
        '''
        getter for the ID of the Student
        '''
        return self.__ID
    
    def setID(self, ID):
        '''
        setter for the ID of the Student
        '''
        self.__ID = ID
            
    def getName(self):
        '''
        getter for the name of the Student
        '''
        return self.__name
    
    def setName(self, name):
        '''
        setter for the name of the Student
        '''
        self.__name = name
    
    def __eq__(self, other):
        return type(self) == type(other) and \
                self.getID() == other.getID() and \
                self.getName() == other.getName()
    
    def __str__(self):
        return str(self.__ID) + "\t NAME: " + self.__name
    
def testStudent():
    stu = Student(8,"Vasilica")
    assert stu.getID() == 8
    assert stu.getName() == "Vasilica"
    stu.setID(169)
    stu.setName("Gheorghidiu")
    assert stu.getID() == 169
    assert stu.getName() == "Gheorghidiu"

if __name__ == '__main__':
    testStudent()
