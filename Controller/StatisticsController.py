from Repository.GradeRepository import GradeRepository
from Domain.Exceptions import DisciplineException
from Repository.DisciplineRepository import DisciplineRepository
from Repository.StudentRepository import StudentRepository

from SortingFiltering import shellSorted

class StatisticsController:
    '''
    creates a new instance of Statistics Controller
    '''
    def __init__(self, graRepo, disRepo, stuRepo):
        self.__graRepo = graRepo
        self.__disRepo = disRepo
        self.__stuRepo = stuRepo
        
    def byDiscipline(self, disciplineName):
        '''
        displays all students and grades at a given discipline
        Input: disciplineName - str
        Output: a list containing all students and grades at a given discipline
        '''
        resString = []
        if self.__disRepo.findByName(disciplineName) != None:
            for gra in self.__graRepo.getAll():
                if gra.getDiscipline() == disciplineName:
                    resString.append(str(self.__stuRepo.findByID(gra.getStudentID())) + "\t GRADE: " + str(gra.getGrade()))
            return resString
        else:
            raise DisciplineException("Discipline with name " + disciplineName + " does not exist!")

    def alphabeticallyByDiscipline(self, disciplineName):
        '''
        displays alphabetically all students and grades at a given discipline
        Input: disciplineName - str
        Output: a list containing all students and grades at a given discipline sorted alphabetically
        '''
        resString = []
        studentsToSort = []
        if self.__disRepo.findByName(disciplineName) != None:
            
            for gra in self.__graRepo.getAll():
                if gra.getDiscipline() == disciplineName:
                    studentsToSort.append(self.__stuRepo.findByID(gra.getStudentID()))
            
            # studentsToSort.sort(key = lambda x: x.getName()) # used before implementing shellSorted
            for stu in shellSorted(studentsToSort, key = lambda x: x.getName()):
                for gra in self.__graRepo.getAll():
                    if gra.getStudentID() == stu.getID() and gra.getDiscipline() == disciplineName:
                        resString.append(str(stu) + "\t GRADE: " + str(gra.getGrade()))
            return resString
        else:
            raise DisciplineException("Discipline with name " + disciplineName + " does not exist!")
        
    def byGradeByDiscipline(self, disciplineName):
        '''
        displays by grade all students and grades at a given discipline
        Input: disciplineName - str
        Output: a list containing all students and grades at a given discipline sorted by grade
        '''
        resString = []
        gradesToSort = []
        if self.__disRepo.findByName(disciplineName) != None:
            for gra in self.__graRepo.getAll():
                if gra.getDiscipline() == disciplineName:
                    gradesToSort.append(gra)
            # gradesToSort.sort(key = lambda x: x.getGrade()) # used before implementing shellSorted
            for gra in shellSorted(gradesToSort, key = lambda x: x.getGrade()):
                resString.append(str(self.__stuRepo.findByID(gra.getStudentID())) + "\t GRADE: " + str(gra.getGrade()))
            return resString
        else:
            raise DisciplineException("Discipline with name " + disciplineName + " does not exist!")
        
    def byAverageGrades(self):
        '''
        displays by the average grade all students and grades
        Input: disciplineName - str
        Output: a list containing all students and grades sorted by the average grade
        '''
        resTuples = []
        resString = []
        for stu in self.__stuRepo.getAll():
            res = 0
            nr = 0
            for gra in self.__graRepo.getAll():
                if gra.getStudentID() == stu.getID():
                    nr += 1
                    res = res + gra.getGrade()
            if nr != 0:
                res = res/nr
                resTuples.append((stu,res))
        # resTuples.sort(key = lambda x: x[1], reverse = True) # used before implementing shellSorted
        for x in shellSorted(resTuples, key = lambda x: x[1], reverse = True):
            resString.append(str(x[0]) + "\t AVERAGE GRADE: " + str(x[1]))
        return resString
        
def testStatisticsController():
    graRepo = GradeRepository()
    disRepo = DisciplineRepository()
    stuRepo = StudentRepository()
    ctrl = StatisticsController(graRepo, disRepo, stuRepo)
    
    try:
        ctrl.byDiscipline("Algebra")
        assert False
    except DisciplineException:
        assert True
    
    assert ctrl.byAverageGrades() == []
    # here might be written more assertions but the program works for all exceptions and in console too
    
if __name__ == '__main__':
    testStatisticsController()
