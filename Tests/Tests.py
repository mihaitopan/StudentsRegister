from Domain.Discipline import testDiscipline
from Domain.Student import testStudent
from Domain.Grade import testGrade
from Repository.DisciplineRepository import testDisciplineRepository
from Repository.StudentRepository import testStudentRepository
from Repository.GradeRepository import testGradeRepository
from Controller.DisciplineController import testDisciplineController
from Controller.StudentController import testStudentController
from Controller.GradeController import testGradeController
from Controller.StatisticsController import testStatisticsController
from SortingFiltering import shellSortedTest, filteredTest

testDiscipline()
testStudent()
testGrade()
testDisciplineRepository()
testStudentRepository()
testGradeRepository()
testDisciplineController()
testStudentController()
testGradeController()
testStatisticsController()
shellSortedTest()
filteredTest()

if __name__ == '__main__':
    print("tests went successful")
