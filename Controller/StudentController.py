from Domain.Student import Student
from Domain.Exceptions import StudentException
from Repository.StudentRepository import StudentRepository
from Repository.GradeRepository import GradeRepository
from Controller.HistoryController import AddOperation, UpdateOperation, BatchRemoveOperation
from Controller.UndoController import UndoController

from copy import deepcopy

class StudentController:
    '''
    creates a new instance of Student Controller
    '''
    def __init__(self, stuRepo, graRepo, undoCtrl):
        self.__repo = stuRepo
        self.__graRepo = graRepo
        
        # the next attributes are needed for undo
        self.__undoCtrl = undoCtrl
        self.__operations = []  # keeps a list of operations that have modified this controller
        self.__index = 0        # keeps the current index in the list of operations - needed for undo
        
    def addStudent(self, stu):
        '''
        adds a Student to the register
        Input: stu - of type Student
        Output: the Student is added, if there in no other Student with the given ID
        Exceptions: raises StudentException if another Student with the same ID already exists
        '''
        # remove undo indexes
        self.__operations = self.__operations[0:self.__index]
        
        self.__repo.add(stu)
        
        # if no exceptions were raised => record the operation for undo
        self.__operations.append(AddOperation(stu))
        self.__index += 1
        self.__undoCtrl.recordUpdatedController([self])
    
    def updateStudent(self, ID, newName):
        '''
        updates a Student from the register, using its ID
        Input: ID - positive integer, the ID of the Student that must be updated
               newName - the name of the new student
        Output: if such a Student exists, it is updated
        Exceptions: raises StudentException if a Student with the given ID does not exist
        '''
        # remove undo indexes
        self.__operations = self.__operations[0:self.__index]
        
        # get the student before update
        oldStudent = deepcopy(self.__repo.findByID(ID))
        
        self.__repo.update(ID,newName)
    
        # if no exceptions were raised => record the operation for undo
        newStudent = deepcopy(self.__repo.findByID(ID))
        self.__operations.append(UpdateOperation(oldStudent, newStudent))
        self.__index += 1
        self.__undoCtrl.recordUpdatedController([self])
        
    def removeStudent(self, ID):
        '''
        removes a Student from the register, using its ID // removes grades with inputed (student)ID
        Input: ID - positive integer, the ID of the Student that must be removed
        Output: if such a Student exists, it is removed and returned
        Exceptions: raises StudentException if a Student with the given ID does not exist
        '''
        # remove undo indexes
        self.__operations = self.__operations[0:self.__index]
        
        # get the student, before deleting it
        parent = self.__repo.findByID(ID)
        affected = []
        
        toSearchList = deepcopy(self.__graRepo.getAll())
        for gra in toSearchList:
            if gra.getStudentID() == ID:
                # affected grades to delete
                affected.append(gra)
                
                self.__graRepo.removeStudentFromDiscipline(gra.getDiscipline(), gra.getStudentID())

        self.__repo.remove(ID)
    
        # if no exceptions were raised => record the operation for undo
        self.__operations.append(BatchRemoveOperation(parent, affected))
        self.__index += 1
        self.__undoCtrl.recordUpdatedController([self])
    
    def getAll(self):
        '''
        returns the list of students
        '''
        return self.__repo.getAll()
    
    def findStudentByName(self, name):
        '''
        finds all students having the given name
        Input: name - the name of the Student being searched for
        Output: list of students having the given name
        '''
        result = []
        for s in self.__repo.getAll():
            if name.upper() == s.getName().upper():
                result.append(s)
        return result
    
    def __len__(self):
        '''
        returns the size of the list of students
        '''
        return len(self.__repo)
    
    def undo(self):
        """
        undoes the last student operation that changed the set of students
        Returns True if operation was undone, False otherwise.
        """
        if self.__index == 0: # no operation to undo
            return False
    
        self.__index -= 1
        operation = self.__operations[self.__index]
    
        if isinstance(operation, AddOperation):
            self.__repo.remove(operation.getObject().getID())
        elif isinstance(operation, BatchRemoveOperation):
            parent = operation.parent_object
            affected = operation.affected_objects
            
            self.__repo.add(parent)
            for gra in affected:
                self.__graRepo.addStudentToDiscipline(gra.getDiscipline(), gra.getStudentID())
                self.__graRepo.updateGrade(gra.getDiscipline(), gra.getStudentID(), gra.getGrade())
            
        else:
            self.__repo.update(operation.getOldObject().getID(), operation.getOldObject().getName())
            
    def redo(self):
        """
        redoes the last student operation that changed the set of students
        Returns True if operation was redone, False otherwise.
        """
        if self.__index == self.__len__() - 1: # no operation to redo
            return False

        operation = self.__operations[self.__index]
    
        if isinstance(operation, AddOperation):
            self.__repo.add(operation.getObject())
        elif isinstance(operation, BatchRemoveOperation):
            parent = operation.parent_object
            affected = operation.affected_objects
            
            self.__repo.remove(parent.getID())
            for gra in affected:
                self.__graRepo.removeStudentFromDiscipline(gra.getDiscipline(), gra.getStudentID())
            
        else:
            self.__repo.update(operation.getUpdatedObject().getID(), operation.getUpdatedObject().getName())
            
        self.__index += 1
    
def testStudentController():
    stuRepo = StudentRepository()
    graRepo = GradeRepository()
    undoCtrl = UndoController()
    ctrl = StudentController(stuRepo, graRepo, undoCtrl)
    
    s1 = Student(1, "Vasilica")
    s2 = Student(1, "Gheorghidiu")
    
    assert len(ctrl) == 0
    
    ctrl.addStudent(s1)
    assert len(ctrl) == 1
    assert ctrl.findStudentByName("Vasilica") == [s1]
    assert ctrl.findStudentByName("John") == []
    
    try:
        ctrl.addStudent(s1)
        assert False
    except StudentException:
        assert True
        
    try:
        ctrl.addStudent(s2)
        assert False
    except StudentException:
        assert True
        
    s2 = Student(2, "Gheorghidiu")
    ctrl.addStudent(s2)
    assert len(ctrl) == 2
    assert ctrl.findStudentByName("Vasilica") == [s1]
    assert ctrl.findStudentByName("Gheorghidiu") == [s2]
    
    ctrl.updateStudent(2,"Johnny Bravo")
    
    assert len(ctrl) == 2
    ctrl.removeStudent(1)
    assert len(ctrl) == 1
    assert ctrl.findStudentByName("Johnny Bravo") == [s2]
    assert ctrl.findStudentByName("Vasilica") == []
    
    try:
        ctrl.removeStudent(1)
        assert False
    except StudentException:
        assert True
    
    ctrl.removeStudent(2)
    assert len(ctrl) == 0

if __name__ == '__main__':
    testStudentController()

