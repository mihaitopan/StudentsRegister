from Domain.Discipline import testDiscipline
from Domain.Student import testStudent
from Repository.DisciplineRepository import testDisciplineRepository
from Repository.StudentRepository import testStudentRepository
from Controller.DisciplineController import testDisciplineController
from Controller.StudentController import testStudentController

testDiscipline()
testStudent()
testDisciplineRepository()
testStudentRepository()
testDisciplineController()
testStudentController()

if __name__ == '__main__':
    print("tests went successful")
