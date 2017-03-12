from Domain.Discipline import Discipline
from Domain.Exceptions import DisciplineException

class DisciplineRepository:
    def __init__(self):
        '''
        creates an instance of the DisciplineRepository
        '''
        self.__data = []
        
    def __find(self, name):
        '''
        returns the index Discipline having the given name
        Input: name - string, the name of the Discipline that is being searched for
        Output: index - if the Discipline was found, -1 - otherwise 
        '''
        for i in range(len(self.__data)):
            if self.__data[i].getName() == name:
                return i
        return -1
        
    def findByName(self, name):
        '''
        returns the Discipline having the given name
        Input: name - string, the name of the Discipline that is being searched for
        Output: the Discipline, if found or None otherwise
        '''
        indexName = self.__find(name) 
        if indexName == -1:
            return None
        return self.__data[indexName]
    
    def add(self, dis):
        '''
        adds a Discipline to the repository
        Input: dis - object of type Discipline
        Output: the given Discipline is added to the repository, if no other Discipline with the same name exists
        Exceptions: raises DisciplineException if another Discipline with the same name already exists
        '''
        if self.findByName(dis.getName()) != None:
            raise DisciplineException("Discipline with name " + dis.getName() + " already exists!")
        self.__data.append(dis)
    
    def update(self, name, newTeacher):
        '''
        updates a Discipline from the repository, using its name
        Input: name - string, the name of the Discipline that must be updated
               newTeacher - string, updated name of the teacher
        Output: if such a Discipline exists, it is updated
        Exceptions: raises DisciplineException if a Discipline with the given name does not exist
        '''
        indexName = self.__find(name)
        if indexName == -1:
            raise DisciplineException("There is no Discipline with name " + name + "!")
        self.__data[indexName].setTeacher(newTeacher)
        
    def remove(self, name):
        '''
        removes a Discipline from the repository, using its name
        Input: name - string, the name of the Discipline that must be removed
        Output: if such a Discipline exists, it is removed and returned
        Exceptions: raises DisciplineException if a Discipline with the given name does not exist
        '''
        indexName = self.__find(name)
        if indexName == -1:
            raise DisciplineException("The is no Discipline with name " + name + "!")
        #return self.__data.pop(indexName)
        self.__data.pop(indexName)
        
    def __len__(self):
        '''
        returns the size of the list of disciplines
        '''
        return len(self.__data)
    
    def getAll(self):
        '''
        returns the list of disciplines
        '''
        return self.__data

def testDisciplineRepository():
    repo = DisciplineRepository()
    
    d1 = Discipline("maths", "Andrea")
    d2 = Discipline("maths", "Columban")
    
    assert len(repo) == 0
    
    repo.add(d1)
    assert len(repo) == 1
    assert repo.findByName("maths") == d1
    
    try:
        repo.add(d1)
        assert False
    except DisciplineException:
        assert True
        
    try:
        repo.add(d2)
        assert False
    except DisciplineException:
        assert True
        
    d2 = Discipline("physics", "Huber")
    repo.add(d2)
    assert len(repo) == 2
    assert repo.findByName("maths") == d1
    assert repo.findByName("physics") == d2
    
    repo.update("physics","Corega")
    
    assert len(repo) == 2
    repo.remove("maths")
    assert len(repo) == 1
    assert repo.findByName("physics") == d2
    assert repo.findByName("maths") == None
    
    try:
        repo.remove("maths")
        assert False
    except DisciplineException:
        assert True
    
    repo.remove("physics")
    assert len(repo) == 0
    
if __name__ == '__main__':
    testDisciplineRepository()
