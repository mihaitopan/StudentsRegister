class Discipline:
    def __init__(self, name, teacher):
        '''
        creates a new instance of Discipline
        '''
        self.__name = name
        self.__teacher = teacher
        
    def getName(self):
        '''
        returns the name of the Discipline // getter
        '''
        return self.__name
    
    def setName(self, name):
        '''
        sets the name of the Discipline // setter
        '''
        self.__name = name
    
    def getTeacher(self):
        '''
        getter for the teacher of the Discipline
        '''
        return self.__teacher
    
    def setTeacher(self, teacher):
        '''
        setter for the teacher of the Discipline
        '''
        self.__teacher = teacher
    
    def __eq__(self, other):
        return type(self) == type(other) and \
                self.getName() == other.getName() and \
                self.getTeacher() == other.getTeacher()
    
    def __str__(self):
        return "NAME: " + self.__name + "\t TEACHER: " + self.__teacher
    
def testDiscipline():
    dis = Discipline("maths","Andrea")
    assert dis.getName() == "maths"
    assert dis.getTeacher() == "Andrea"
    dis.setName("physics")
    dis.setTeacher("Corega")
    assert dis.getName() == "physics"
    assert dis.getTeacher() == "Corega"

if __name__ == '__main__':
    testDiscipline()
