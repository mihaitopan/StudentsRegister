# go for it: before each verification: from Tests.Tests import *

from Domain.Discipline import Discipline
from Domain.Student import Student
from Repository.DisciplineRepository import DisciplineRepository
from Repository.StudentRepository import StudentRepository
from Repository.GradeRepository import GradeRepository
from Repository.FileDisciplineRepository import FileDisciplineRepository
from Repository.FileStudentRepository import FileStudentRepository
from Repository.FileGradeRepository import FileGradeRepository
from Controller.DisciplineController import DisciplineController
from Controller.StudentController import StudentController
from Controller.GradeController import GradeController
from Controller.StatisticsController import StatisticsController
from Controller.UndoController import UndoController
from UI.UI import UI

option = input("Do you want to operate (load/store information) with the file?  If yes, type 'yes'. Otherwise, type anything else: ")

if option == "yes":
    repoDiscipline = FileDisciplineRepository()
    repoStudent = FileStudentRepository()
    repoGrade = FileGradeRepository()

else:
    repoDiscipline = DisciplineRepository()
    repoStudent = StudentRepository()
    repoGrade = GradeRepository()
    
    # add initial data
    repoDiscipline.add(Discipline("Algebra", "Crivei"))
    repoDiscipline.add(Discipline("Analysis", "no ideea"))
    repoDiscipline.add(Discipline("Computational Logic", "Lupea"))
    repoDiscipline.add(Discipline("Computational Systems Architecture", "Vancea"))
    repoDiscipline.add(Discipline("Fundamentals of Programming", "Arthur"))
    repoDiscipline.add(Discipline("Communication and Personal Development in Computer Science", "Motogna"))
    
    repoStudent.add(Student(1, "Harap-Alb"))
    repoStudent.add(Student(2, "Bestia"))
    repoStudent.add(Student(3, "Luceafarul"))
    repoStudent.add(Student(4, "Afrodita"))
    repoStudent.add(Student(5, "Shrek"))
    repoStudent.add(Student(6, "Bula"))
    
    repoGrade.addStudentToDiscipline("Algebra", 1)
    repoGrade.addStudentToDiscipline("Analysis", 1)
    repoGrade.addStudentToDiscipline("Computational Logic", 1)
    repoGrade.addStudentToDiscipline("Computational Systems Architecture", 1)
    repoGrade.addStudentToDiscipline("Fundamentals of Programming", 1)
    repoGrade.addStudentToDiscipline("Communication and Personal Development in Computer Science", 1)
    repoGrade.addStudentToDiscipline("Algebra", 2)
    repoGrade.addStudentToDiscipline("Analysis", 2)
    repoGrade.addStudentToDiscipline("Computational Logic", 2)
    repoGrade.addStudentToDiscipline("Computational Systems Architecture", 2)
    repoGrade.addStudentToDiscipline("Fundamentals of Programming", 2)
    repoGrade.addStudentToDiscipline("Communication and Personal Development in Computer Science", 2)
    repoGrade.addStudentToDiscipline("Algebra", 3)
    repoGrade.addStudentToDiscipline("Analysis", 3)
    repoGrade.addStudentToDiscipline("Computational Logic", 3)
    repoGrade.addStudentToDiscipline("Computational Systems Architecture", 4)
    repoGrade.addStudentToDiscipline("Fundamentals of Programming", 4)
    repoGrade.addStudentToDiscipline("Communication and Personal Development in Computer Science", 4)
    repoGrade.addStudentToDiscipline("Algebra", 5)
    repoGrade.addStudentToDiscipline("Analysis", 6)
    repoGrade.addStudentToDiscipline("Computational Logic", 5)
    repoGrade.addStudentToDiscipline("Computational Systems Architecture", 6)
    repoGrade.addStudentToDiscipline("Fundamentals of Programming", 5)
    repoGrade.addStudentToDiscipline("Communication and Personal Development in Computer Science", 6)
    repoGrade.updateGrade("Algebra", 1, 9.9)
    repoGrade.updateGrade("Analysis", 1, 7.8)
    repoGrade.updateGrade("Computational Logic", 1, 5.7)
    repoGrade.updateGrade("Computational Systems Architecture", 1, 6.2)
    repoGrade.updateGrade("Fundamentals of Programming", 1, 10)
    repoGrade.updateGrade("Communication and Personal Development in Computer Science", 1, 10)
    repoGrade.updateGrade("Algebra", 2, 9.2)
    repoGrade.updateGrade("Analysis", 2, 9.7)
    repoGrade.updateGrade("Computational Logic", 2, 3.8)
    repoGrade.updateGrade("Computational Systems Architecture", 2, 2.8)
    repoGrade.updateGrade("Fundamentals of Programming", 2, 10)
    repoGrade.updateGrade("Communication and Personal Development in Computer Science", 2, 10)
    repoGrade.updateGrade("Algebra", 3, 7.3)
    repoGrade.updateGrade("Analysis", 3, 6.0)
    repoGrade.updateGrade("Computational Logic", 3, 8.2)
    repoGrade.updateGrade("Computational Systems Architecture", 4, 9.0)
    repoGrade.updateGrade("Fundamentals of Programming", 4, 9.9)
    repoGrade.updateGrade("Communication and Personal Development in Computer Science", 4, 10)
    repoGrade.updateGrade("Algebra", 5, 8.9)
    repoGrade.updateGrade("Analysis", 6, 9.3)
    repoGrade.updateGrade("Computational Logic", 5, 8.6)
    repoGrade.updateGrade("Computational Systems Architecture", 6, 7.5)
    repoGrade.updateGrade("Fundamentals of Programming", 5, 9.6)
    repoGrade.updateGrade("Communication and Personal Development in Computer Science", 6, 10)
    # initial data added

ctrlUndo = UndoController()
ctrlDiscipline = DisciplineController(repoDiscipline, repoGrade, ctrlUndo)
ctrlStudent = StudentController(repoStudent, repoGrade, ctrlUndo)
ctrlGrade = GradeController(repoGrade, repoDiscipline, repoStudent, ctrlUndo)
ctrlStatistics = StatisticsController(repoGrade, repoDiscipline, repoStudent)

ui = UI(ctrlDiscipline, ctrlStudent, ctrlGrade, ctrlStatistics, ctrlUndo)

ui.mainMenu()