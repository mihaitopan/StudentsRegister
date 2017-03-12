from Domain.Discipline import Discipline
from Domain.Exceptions import DisciplineException
from Repository.DisciplineRepository import DisciplineRepository
from Repository.GradeRepository import GradeRepository
from Controller.HistoryController import AddOperation, UpdateOperation, BatchRemoveOperation
from Controller.UndoController import UndoController

from copy import deepcopy

class DisciplineController:
    '''
    creates a new instance of Discipline Controller
    '''
    def __init__(self, disRepo, graRepo, undoCtrl):
        self.__repo = disRepo
        self.__graRepo = graRepo
        
        # the next attributes are needed for undo
        self.__undoCtrl = undoCtrl
        self.__operations = []  # keeps a list of operations that have modified this controller
        self.__index = 0        # keeps the current index in the list of operations - needed for undo
        
    def addDiscipline(self, dis):
        '''
        adds a Discipline to the register
        Input: dis - of type Discipline
        Output: the Discipline is added, if there in no other Discipline with the given name
        Exceptions: raises DisciplineException if another Discipline with the same name already exists
        '''
        # remove undo indexes
        self.__operations = self.__operations[0:self.__index]
        
        self.__repo.add(dis)
        
        # if no exceptions were raised => record the operation for undo
        self.__operations.append(AddOperation(dis))
        self.__index += 1
        self.__undoCtrl.recordUpdatedController([self])
    
    def updateDiscipline(self, name, newTeacherName):
        '''
        updates a Discipline from the register, using its name
        Input: name - positive integer, the name of the Discipline that must be updated
               newTeacherName - the name of the new teacher
        Output: if such a Discipline exists, it is updated
        Exceptions: raises DisciplineException if a Discipline with the given name does not exist
        '''
        # remove undo indexes
        self.__operations = self.__operations[0:self.__index]
        
        # get the discipline before update
        oldDiscipline = deepcopy(self.__repo.findByName(name))

        self.__repo.update(name,newTeacherName)
    
        # if no exceptions were raised => record the operation for undo
        newDiscipline = deepcopy(self.__repo.findByName(name))

        self.__operations.append(UpdateOperation(oldDiscipline, newDiscipline))
        self.__index += 1
        self.__undoCtrl.recordUpdatedController([self])
        
    def removeDiscipline(self, name):
        '''
        removes a Discipline from the register, using its name // removes grades with inputed discipline
        Input: name - positive integer, the name of the Discipline that must be removed
        Output: if such a Discipline exists, it is removed and returned
        Exceptions: raises DisciplineException if a Discipline with the given name does not exist
        '''
        # remove undo indexes
        self.__operations = self.__operations[0:self.__index]
        
        # get the discipline, before deleting it
        parent = self.__repo.findByName(name)
        affected = []
        
        toSearchList = deepcopy(self.__graRepo.getAll())
        for gra in toSearchList:
            if gra.getDiscipline() == name:
                # affected grades to delete
                affected.append(gra)
                                
                self.__graRepo.removeStudentFromDiscipline(gra.getDiscipline(), gra.getStudentID())
                
        self.__repo.remove(name)
    
        # if no exceptions were raised => record the operation for undo
        self.__operations.append(BatchRemoveOperation(parent, affected))
        self.__index += 1
        self.__undoCtrl.recordUpdatedController([self])
    
    def getAll(self):
        '''
        returns the list of disciplines
        '''
        return self.__repo.getAll()
    
    def findDisciplineByTeacher(self, teacher):
        '''
        finds all disciplines having the given teacher
        Input: teacher - the teacher of the Discipline being searched for
        Output: list of disciplines having the given teacher
        '''
        result = []
        for dis in self.__repo.getAll():
            if teacher.upper() == dis.getTeacher().upper():
                result.append(dis)
        return result
    
    def __len__(self):
        '''
        returns the size of the list of disciplines
        '''
        return len(self.__repo)
    
    def undo(self):
        """
        undoes the last discipline operation that changed the set of disciplines
        Returns True if operation was undone, False otherwise.
        """
        if self.__index == 0: # no operation to undo
            return False
    
        self.__index -= 1
        operation = self.__operations[self.__index]
    
        if isinstance(operation, AddOperation):
            self.__repo.remove(operation.getObject().getName())
        elif isinstance(operation, BatchRemoveOperation):
            parent = operation.parent_object
            affected = operation.affected_objects
            
            self.__repo.add(parent)
            for gra in affected:
                self.__graRepo.addStudentToDiscipline(gra.getDiscipline(), gra.getStudentID())
                self.__graRepo.updateGrade(gra.getDiscipline(), gra.getStudentID(), gra.getGrade())
         
        else:
            self.__repo.update(operation.getOldObject().getName(), operation.getOldObject().getTeacher())           
            
    def redo(self):
        """
        redoes the last discipline operation that changed the set of disciplines
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
            
            self.__repo.remove(parent.getName())
            for gra in affected:
                self.__graRepo.removeStudentFromDiscipline(gra.getDiscipline(), gra.getStudentID())
         
        else:
            self.__repo.update(operation.getUpdatedObject().getName(), operation.getUpdatedObject().getTeacher())
            
        self.__index += 1
    
def testDisciplineController():
    disRepo = DisciplineRepository()
    graRepo = GradeRepository()
    undoCtrl = UndoController()
    ctrl = DisciplineController(disRepo, graRepo, undoCtrl)
    
    d1 = Discipline("maths", "Andrea")
    d2 = Discipline("maths", "Columban")
    
    assert len(ctrl) == 0
    
    ctrl.addDiscipline(d1)
    assert len(ctrl) == 1
    assert ctrl.findDisciplineByTeacher("Andrea") == [d1]
    
    try:
        ctrl.addDiscipline(d1)
        assert False
    except DisciplineException:
        assert True
        
    try:
        ctrl.addDiscipline(d2)
        assert False
    except DisciplineException:
        assert True
        
    d2 = Discipline("physics", "Huber")
    ctrl.addDiscipline(d2)
    assert len(ctrl) == 2
    assert ctrl.findDisciplineByTeacher("Andrea") == [d1]
    assert ctrl.findDisciplineByTeacher("Huber") == [d2]
    
    ctrl.updateDiscipline("physics","Corega")
    
    assert len(ctrl) == 2
    ctrl.removeDiscipline("maths")
    assert len(ctrl) == 1
    assert ctrl.findDisciplineByTeacher("Corega") == [d2]
    assert ctrl.findDisciplineByTeacher("Andrea") == []
    
    try:
        ctrl.removeDiscipline("maths")
        assert False
    except DisciplineException:
        assert True
    
    ctrl.removeDiscipline("physics")
    assert len(ctrl) == 0
    
if __name__ == '__main__':
    testDisciplineController()
