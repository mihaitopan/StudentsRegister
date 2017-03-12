from Repository.DisciplineRepository import DisciplineRepository
from Domain.Discipline import Discipline

class FileDisciplineRepository(DisciplineRepository):

    def __init__(self, fname="Repository\\storedDisciplines.txt"):
        self._fName = fname
        DisciplineRepository.__init__(self)
        self._loadFromFile()

    def add(self, dis):
        '''
        adds a discipline to the DisciplineRepository
        Input: dis - discipline object
        Output: stores the added discipline to the file
        '''
        DisciplineRepository.add(self, dis)
        self._storeToFile()

    def update(self, name, newTeacher):
        '''
        updates a discipline in the DisciplineRepository
        Input: name - string, newTeacher - string
        Output: updates the updated discipline in the file
        '''
        DisciplineRepository.update(self, name, newTeacher)
        self._storeToFile()

    def remove(self, name):
        '''
        removes a discipline in the DisciplineRepository
        Input: name - string
        Output: removes the removed discipline from the file
        '''
        dis = DisciplineRepository.remove(self, name)
        self._storeToFile()
        return dis

    def _storeToFile(self):
        '''
        stores information to the file
        Input: -
        Output: stored information
        '''
        f = open(self._fName, "w")
        disciplines = DisciplineRepository.getAll(self)
        for dis in disciplines:
            disf = dis.getName() + ";" + dis.getTeacher() + "\n"
            f.write(disf)
        f.close()

    def _loadFromFile(self):
        '''
        loads information from the file
        Input: -
        Output: loaded information
        '''
        try:
            f = open(self._fName, "r")
        except IOError:
            return
        line = f.readline().strip()
        while line != "":
            t = line.split(";")
            dis = Discipline(t[0], t[1])
            self.add(dis)
            line = f.readline().strip()
        f.close()
    