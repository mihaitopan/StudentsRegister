from Repository.StudentRepository import StudentRepository
from Domain.Student import Student

class FileStudentRepository(StudentRepository):

    def __init__(self, fname="Repository\\storedStudents.txt"):
        self._fName  = fname
        StudentRepository.__init__(self)
        self._loadFromFile()

    def add(self, stu):
        '''
        adds a student to the StudentRepository
        Input: stu - student object
        Output: stores the added student to the file
        '''
        StudentRepository.add(self, stu)
        self._storeToFile()

    def update(self, ID, newName):
        '''
        updates a student in the StudentRepository
        Input: ID - integer, newName - string
        Output: updates the updated student to the file
        '''
        StudentRepository.update(self, ID, newName)
        self._storeToFile()

    def remove(self, ID):
        '''
        removes a student from the StudentRepository
        Input: ID - integer
        Output: removes the removed student from the file
        '''
        stu = StudentRepository.remove(self, ID)
        self._storeToFile()
        return stu

    def _storeToFile(self):
        '''
        stores information to the file
        Input: -
        Output: stored information
        '''
        f = open(self._fName, "w")
        students = StudentRepository.getAll(self)
        for stu in students:
            stuf = str(stu.getID()) + ";" + stu.getName() + "\n"
            f.write(stuf)
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
            print("de")
            return
        line = f.readline().strip()
        while line != "":
            t = line.split(";")
            stu = Student(int(t[0]), t[1])
            self.add(stu)
            line = f.readline().strip()
        f.close()
    