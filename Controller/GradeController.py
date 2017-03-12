from Domain.Exceptions import GradeException
from Repository.GradeRepository import GradeRepository
from Domain.Grade import Grade

from copy import deepcopy

from Domain.Discipline import Discipline
from Domain.Student import Student
from Domain.Exceptions import DisciplineException
from Domain.Exceptions import StudentException
from Repository.DisciplineRepository import DisciplineRepository
from Repository.StudentRepository import StudentRepository
from Controller.HistoryController import AddOperation, RemoveOperation, UpdateOperation
from Controller.UndoController import UndoController

class GradeController:
    '''
    creates a new instance of Grade Controller
    '''
    def __init__(self, graRepo, disRepo, stuRepo, undoCtrl):
        self.__repo = graRepo
        self.__disRepo = disRepo
        self.__stuRepo = stuRepo
        
        # the next attributes are needed for undo
        self.__undoCtrl = undoCtrl
        self.__operations = []  # keeps a list of operations that have modified this controller
        self.__index = 0        # keeps the current index in the list of operations - needed for undo
        
    def addStudentToDiscipline(self, discipline, studentID):
        '''
        adds a student to a discipline
        Input: discipline - string, the name of the discipline that the student must be added to
               studentID - positive integer, the ID of the student to add to the discipline
        Output: the given Grade is added, if no other Grade with the same discipline and studentID exists
                ! the given Grade's grade is initialized with 0
        Exceptions: raises DisciplineException if the given discipline's name does not exist in DisciplineRepository
                    raises StudentException if the given student's ID does not exist in StudentRepository
                    raises GradeException if another Grade with the same discipline and studentID already exists            
        '''
        # remove undo indexes
        self.__operations = self.__operations[0:self.__index]
        
        if self.__disRepo.findByName(discipline) == None:
            raise DisciplineException("There is no Discipline with name " + discipline + "!")
        if self.__stuRepo.findByID(studentID) == None:
            raise StudentException("The is no Student with ID " + str(studentID) + "!")
        self.__repo.addStudentToDiscipline(discipline, studentID)
        
        gra = Grade(discipline, studentID, 0)
        # if no exceptions were raised => record the operation for undo
        self.__operations.append(AddOperation(gra))
        self.__index += 1
        self.__undoCtrl.recordUpdatedController([self])
    
    def updateGrade(self, discipline, studentID, grade):
        '''
        updates a Grade's grade
        Input: discipline - string, the name of the discipline that the student must be added to
               studentID - positive integer, the ID of the student to add to a discipline
               grade - float, 1<= grade <= 10, the grade to be updated
        Output: if such a Grade exists, it is updated
        Exceptions: raises DisciplineException if the given discipline's name does not exist in DisciplineRepository
                    raises StudentException if the given student's ID does not exist in StudentRepository
                    raises GradeException if a Grade with the given discipline and studentID does not exist
        '''
        # remove undo indexes
        self.__operations = self.__operations[0:self.__index]
        
        if self.__disRepo.findByName(discipline) == None:
            raise DisciplineException("There is no Discipline with name " + discipline + "!")
        if self.__stuRepo.findByID(studentID) == None:
            raise StudentException("The is no Student with ID " + str(studentID) + "!")
        
        # get the grade before update
        oldGrade = deepcopy(self.__repo.findByDisciplineAndStudentID(discipline, studentID))
        
        self.__repo.updateGrade(discipline, studentID, grade)
        
        # if no exceptions were raised => record the operation for undo
        newGrade = deepcopy(self.__repo.findByDisciplineAndStudentID(discipline, studentID))
        self.__operations.append(UpdateOperation(oldGrade, newGrade))
        self.__index += 1
        self.__undoCtrl.recordUpdatedController([self])
        
    def removeStudentFromDiscipline(self, discipline, studentID):
        '''
        removes a student from a discipline
        Input: discipline - string, the name of the discipline that the student must be removed from
               studentID - positive integer, the ID of the student to remove from the discipline
        Output: if such a Grade exists, it is removed and returned
        Exceptions: raises DisciplineException if the given discipline's name does not exist in DisciplineRepository
                    raises StudentException if the given student's ID does not exist in StudentRepository
                    raises GradeException if a Grade with the given discipline and studentID does not exist
        '''
        # remove undo indexes
        self.__operations = self.__operations[0:self.__index]
        
        if self.__disRepo.findByName(discipline) == None:
            raise DisciplineException("There is no Discipline with name " + discipline + "!")
        if self.__stuRepo.findByID(studentID) == None:
            raise StudentException("The is no Student with ID " + str(studentID) + "!")
        
        # get the grade before deleting it
        gra = self.__repo.findByDisciplineAndStudentID(discipline, studentID)
        
        self.__repo.removeStudentFromDiscipline(discipline, studentID)
    
        # if no exceptions were raised => record the operation for undo
        self.__operations.append(RemoveOperation(gra))
        self.__index += 1
        self.__undoCtrl.recordUpdatedController([self])
    
    def getAll(self):
        '''
        returns the list of Grades
        '''
        return self.__repo.getAll()
    
    def __len__(self):
        '''
        returns the size of the list of Grades
        '''
        return len(self.__repo)
    
    def undo(self):
        """
        undoes the last grade operation that changed the set of grades
        Returns True if operation was undone, False otherwise.
        """
        if self.__index == 0: # no operation to undo
            return False
    
        self.__index -= 1
        operation = self.__operations[self.__index]
    
        if isinstance(operation, AddOperation):
            self.__repo.removeStudentFromDiscipline(operation.getObject().getDiscipline(), operation.getObject().getStudentID())
        elif isinstance(operation, RemoveOperation):
            self.__repo.addStudentToDiscipline(operation.getObject().getDiscipline(), operation.getObject().getStudentID())
        else:
            self.__repo.updateGrade(operation.getOldObject().getDiscipline(), operation.getOldObject().getStudentID(), operation.getOldObject().getGrade())
            
    def redo(self):
        """
        redoes the last grade operation that changed the set of grades
        Returns True if operation was redone, False otherwise.
        """
        if self.__index == self.__len__() - 1: # no operation to redo
            return False

        operation = self.__operations[self.__index]
    
        if isinstance(operation, AddOperation):
            self.__repo.addStudentToDiscipline(operation.getObject().getDiscipline(), operation.getObject().getStudentID())
        elif isinstance(operation, RemoveOperation):
            self.__repo.removeStudentFromDiscipline(operation.getObject().getDiscipline(), operation.getObject().getStudentID())
        else:
            self.__repo.updateGrade(operation.getUpdatedObject().getDiscipline(), operation.getUpdatedObject().getStudentID(), operation.getUpdatedObject().getGrade())
            
        self.__index += 1
    
def testGradeController():
    graRepo = GradeRepository()
    disRepo = DisciplineRepository()
    stuRepo = StudentRepository()
    undoCtrl = UndoController()
    ctrl = GradeController(graRepo, disRepo, stuRepo, undoCtrl)
    
    assert len(ctrl) == 0
    
    try:
        ctrl.addStudentToDiscipline("maths", 1)
        assert False
    except (DisciplineException, StudentException):
        assert True
    
    try:
        ctrl.updateGrade("maths", 1, 0)
        assert False
    except (DisciplineException, StudentException):
        assert True
    
    try:
        ctrl.removeStudentFromDiscipline("maths", 1)
        assert False
    except (DisciplineException, StudentException):
        assert True

    d1 = Discipline("maths", "Andrea")
    disRepo.add(d1)
    assert disRepo.findByName("maths") == d1
    s1 = Student(1,"Harap-Alb")
    stuRepo.add(s1)
    assert stuRepo.findByID(1) == s1
            
    ctrl.addStudentToDiscipline("maths", 1)
        
    assert len(ctrl) == 1

    try:
        ctrl.addStudentToDiscipline("maths", 1)
        assert False
    except GradeException:
        assert True
        
    try:
        ctrl.updateGrade("maths", 8, 10)
        assert False
    except (GradeException, DisciplineException, StudentException):
        assert True
     
    ctrl.updateGrade("maths", 1, 10)
    assert len(ctrl) == 1

    ctrl.removeStudentFromDiscipline("maths", 1)
    assert len(ctrl) == 0
    
    try:
        ctrl.removeStudentFromDiscipline("maths", 1)
        assert False
    except GradeException:
        assert True

if __name__ == '__main__':
    testGradeController()
    print("success")
