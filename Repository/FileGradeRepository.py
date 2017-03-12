from Repository.GradeRepository import GradeRepository

class FileGradeRepository(GradeRepository):

    def __init__(self, fname="Repository\\storedGrades.txt"):
        self._fName = fname
        super().__init__() # super - alternative method of GradeRepository.__init__(self)
        self._loadFromFile()

    def addStudentToDiscipline(self, discipline, studentID):
        '''
        adds a grade to the GradeRepository
        Input: discipline - string, studentID - integer
        Output: stores the added grade to the file
        '''
        super().addStudentToDiscipline(discipline, studentID)
        self._storeToFile()

    def updateGrade(self, discipline, studentID, grade):
        '''
        updates a grade in the GradeRepository
        Input: discipline - string, studentID - integer, grade - float
        Output: updates the updated grade in the file
        '''
        super().updateGrade(discipline, studentID, grade)
        self._storeToFile()

    def removeStudentFromDiscipline(self, discipline, studentID):
        '''
        removes a grade from the GradeRepository
        Input: discipline - string, studentID - integer
        Output: removes the added grade to the file
        '''
        gra = super().removeStudentFromDiscipline(discipline, studentID)
        self._storeToFile()
        return gra

    def _storeToFile(self):
        '''
        stores information to the file
        Input: -
        Output: stored information
        '''
        f = open(self._fName, "w")
        grades = GradeRepository.getAll(self)
        for gra in grades:
            graf = gra.getDiscipline() + ";" + str(gra.getStudentID()) + ";" + str(gra.getGrade()) + "\n"
            f.write(graf)
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
            self.addStudentToDiscipline(t[0], int(t[1]))
            self.updateGrade(t[0], int(t[1]), float(t[2]))
            line = f.readline().strip()
        f.close()
    