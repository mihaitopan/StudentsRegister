from Domain.Discipline import Discipline
from Domain.Student import Student
from Domain.Exceptions import DisciplineException, StudentException, GradeException

class UI:
    def __init__(self, disController, stuController, graController, staController, undoController):
        self.__disCtrl = disController
        self.__stuCtrl = stuController
        self.__graCtrl = graController
        self.__staCtrl = staController
        self.__undoCtrl = undoController
        
    @staticmethod
    def printMenu():
        printStr = 'Available commands:\n'
        printStr += '\t 1 - Manage disciplines \n'
        printStr += '\t 2 - Manage students \n'
        printStr += '\t 3 - Manage grades \n'
        printStr += '\t 4 - Display statistics \n'
        printStr += '\t 5 - Undo the last operation \n'
        printStr += '\t 6 - Redo the last operation \n'
        printStr += '\t 0 - Exit \n'
        print(printStr)
    
    @staticmethod  
    def validInputCommand(command):
        '''
        verifies if the given command is a valid one
        Input: command - the given command - a string
        Output: True - if the command ID valid
                False - otherwise
        Exceptions: -
        '''
        availableCommands = ['1', '2', '3', '4', '5', '6', '0'];
        return (command in availableCommands)
    
    @staticmethod
    def printDisciplineMenu():
        printStr = '\nAvailable commands:\n'
        printStr += '\t 1 - Add discipline \n'
        printStr += '\t 2 - Update discipline \n'
        printStr += '\t 3 - Remove discipline \n'
        printStr += '\t 4 - Search discipline by teacher \n'
        printStr += '\t 5 - Display all disciplines \n'
        printStr += '\t 0 - Back to Main Menu \n'
        print(printStr)
    
    @staticmethod  
    def validInputDisciplineCommand(command):
        '''
        verifies if the given command is a valid one
        Input: command - the given command - a string
        Output: True - if the command ID valid
                False - otherwise
        Exceptions: -
        '''
        availableCommands = ['1', '2', '3', '4', '5', '0'];
        return (command in availableCommands)
    
    @staticmethod
    def printStundentMenu():
        printStr = '\nAvailable commands:\n'
        printStr += '\t 1 - Add student \n'
        printStr += '\t 2 - Update student \n'
        printStr += '\t 3 - Remove student \n'
        printStr += '\t 4 - Search student by name \n'
        printStr += '\t 5 - Display all students \n'
        printStr += '\t 0 - Back to Main Menu \n'
        print(printStr)
    
    @staticmethod  
    def validInputStudentCommand(command):
        '''
        verifies if the given command is a valid one
        Input: command - the given command - a string
        Output: True - if the command ID valid
                False - otherwise
        Exceptions: -
        '''
        availableCommands = ['1', '2', '3', '4', '5', '0'];
        return (command in availableCommands)
    
    @staticmethod
    def printGradeMenu():
        printStr = '\nAvailable commands:\n'
        printStr += '\t 1 - Add student to a discipline \n'
        printStr += '\t 2 - Update a grade \n'
        printStr += '\t 3 - Remove student from a discipline \n'
        printStr += '\t 4 - Display all grades \n'
        printStr += '\t 0 - Back to Main Menu \n'
        print(printStr)
    
    @staticmethod  
    def validInputGradeCommand(command):
        '''
        verifies if the given command is a valid one
        Input: command - the given command - a string
        Output: True - if the command ID valid
                False - otherwise
        Exceptions: -
        '''
        availableCommands = ['1', '2', '3', '4', '0'];
        return (command in availableCommands)
    
    @staticmethod
    def printStatisticsMenu():
        printStr = '\nAvailable commands:\n'
        printStr += '\t 1 - Display students at a discipline \n'
        printStr += '\t 2 - Display students alphabetically at a discipline \n'
        printStr += '\t 3 - Display students by grade at a discipline \n'
        printStr += '\t 4 - Display students by average grade \n'
        printStr += '\t 0 - Back to Main Menu \n'
        print(printStr)
    
    @staticmethod  
    def validInputStatisticsCommand(command):
        '''
        verifies if the given command is a valid one
        Input: command - the given command - a string
        Output: True - if the command ID valid
                False - otherwise
        Exceptions: -
        '''
        availableCommands = ['1', '2', '3', '4', '0'];
        return (command in availableCommands)
    
    @staticmethod
    def readPositiveInteger(msg):
        '''
        reads a positive integer
        Input: msg - the message to be shown to the user before reading
        Output: A positive integer 
        Exceptions: -
        '''
        res = 0
        while True:
            try:
                res = int(input(msg))
                if res < 0:
                    raise ValueError()
                break
            except ValueError:
                print("The value you introduced is NOT a positive integer.")
        return res
    
    @staticmethod
    def readGrade(msg):
        '''
        reads a float number between 1 and 10
        Input: msg - the message to be shown to the user before reading
        Output: a float number between 1 and 10
        Exceptions: -
        '''
        res = 0
        while True:
            try:
                res = float(input(msg))
                if res < 1 or res > 10:
                    raise ValueError()
                break
            except ValueError:
                print("The value you introduced is NOT a number between 1 and 10.")
        return res
    
    # Disciplines
    def __addDisciplineMenu(self):
        '''
        adds a Discipline to the register
        Input: -
        Output: a new Discipline is read and added (if there is no other Discipline with the same name)
        '''
        name = input("Please enter the Discipline name: ")
        teacher = input("Please enter the Discipline teacher: ")
    
        try:
            dis = Discipline(name, teacher)
            self.__disCtrl.addDiscipline(dis)
        except DisciplineException as ex:
            print(ex)
            
    def __updateDisciplineMenu(self):
        '''
        updates a Discipline from the register
        Input: -
        Output: the Discipline is updated, if it exists
        '''
        name = input("Please enter the Discipline name: ")
        newTeacher = input("Please enter the Discipline's new teacher: ")
        
        try:
            self.__disCtrl.updateDiscipline(name, newTeacher)
        except DisciplineException as ex:
            print(ex)
        
    def __removeDisciplineMenu(self):
        '''
        removes a Discipline from the register
        Input: -
        Output: the Discipline is removed, if it exists
        '''
        name = input("Please enter the Discipline name: ")
        
        try:
            self.__disCtrl.removeDiscipline(name)
        except (DisciplineException, GradeException) as ex:
            print(ex)
                
    def __findDisciplineByTeacherMenu(self):
        '''
        finds disciplines by teacher
        Input: -
        Output: a list of disciplines having the teacher that is being searched for is shown
        '''
        teacher = input("Please enter the Discipline teacher: ")
        res = self.__disCtrl.findDisciplineByTeacher(teacher)
        if res == []:
            print("There are no disciplines with the given teacher.")
        else:
            print("Found disciplines: ")
            for e in res:
                print(e)
          
    def __showAllDisciplinesMenu(self):
        diss = self.__disCtrl.getAll()
        if len(diss) == 0:
            print("There are no disciplines in the register.")
        else:
            for e in diss:
                print(e)
    
    def disciplineMenu(self):
        commandDict = {'1': self.__addDisciplineMenu,
                       '2': self.__updateDisciplineMenu,
                       '3': self.__removeDisciplineMenu,
                       '4': self.__findDisciplineByTeacherMenu,
                       '5': self.__showAllDisciplinesMenu}
        while True:
            UI.printDisciplineMenu()
            command = input("Please enter your command: ")
            while not UI.validInputDisciplineCommand(command):
                print("Please enter a valid command!")
                command = input("Please enter your command: ")
            if command == '0':
                return
            commandDict[command]()
    
    # Students
    def __addStudentMenu(self):
        '''
        adds a Student to the register
        Input: -
        Output: a new Student is read and added (if there is no other Student with the same name)
        '''
        ID = UI.readPositiveInteger("Please enter the Student ID: ")
        name = input("Please enter the Student name: ")
    
        try:
            stu = Student(ID, name)
            self.__stuCtrl.addStudent(stu)
        except StudentException as ex:
            print(ex)
            
    def __updateStudentMenu(self):
        '''
        updates a Student from the register
        Input: -
        Output: the Student is updated, if it exists
        '''
        ID = UI.readPositiveInteger("Please enter the Student ID: ")
        name = input("Please enter the Student's name: ")
        
        try:
            self.__stuCtrl.updateStudent(ID, name)
        except StudentException as ex:
            print(ex)
        
    def __removeStudentMenu(self):
        '''
        removes a Student from the register
        Input: -
        Output: the Student is removed, if it exists
        '''
        ID = UI.readPositiveInteger("Please enter the Student ID: ")
        
        try:
            self.__stuCtrl.removeStudent(ID)
        except (StudentException, GradeException) as ex:
            print(ex)
                
    def __findStudentByNameMenu(self):
        '''
        finds students by name
        Input: -
        Output: a list of students having the name that is being searched for is shown
        '''
        name = input("Please enter the Student's name: ")
        res = self.__stuCtrl.findStudentByName(name)
        if res == []:
            print("There are no students with the given name.")
        else:
            print("Found students: ")
            for e in res:
                print(e)
          
    def __showAllStudentsMenu(self):
        stus = self.__stuCtrl.getAll()
        if len(stus) == 0:
            print("There are no students in the register.")
        else:
            for e in stus:
                print(e)
    
    def studentMenu(self):
        commandDict = {'1': self.__addStudentMenu,
                       '2': self.__updateStudentMenu,
                       '3': self.__removeStudentMenu,
                       '4': self.__findStudentByNameMenu,
                       '5': self.__showAllStudentsMenu}
        while True:
            UI.printStundentMenu()
            command = input("Please enter your command: ")
            while not UI.validInputStudentCommand(command):
                print("Please enter a valid command!")
                command = input("Please enter your command: ")
            if command == '0':
                return
            commandDict[command]()
    
    # Grades
    def __addStudentToDiscipline(self):
        '''
        adds a student to a discipline
        Input: -
        Output: a student and a discipline are read and added to a grade
        '''
        discipline = input("Please enter discipline's name:")
        studentID = UI.readPositiveInteger("Please enter the student's ID: ")
        try:
            self.__graCtrl.addStudentToDiscipline(discipline, studentID)
            print("Student's grade will be initialized with 0. Please go to update grade to change it.")
        except (DisciplineException, StudentException, GradeException) as ex:
            print(ex)
        
    def __updateGrade(self):
        '''
        adds a grade to student at a discipline
        Input: -
        Output: a grade is read and added to a to student at a discipline
        '''
        discipline = input("Please enter discipline's name:")
        studentID = UI.readPositiveInteger("Please enter the student's ID: ")
        grade = UI.readGrade("Please enter the student's grade: ")
        try:
            self.__graCtrl.updateGrade(discipline, studentID, grade)
        except (DisciplineException, StudentException, GradeException) as ex:
            print(ex)
    
    def __removeStudentFromDiscipline(self):
        '''
        removes a student from a discipline // a Grade in fact
        Input: -
        Output: the Grade is removed if exists
        '''
        discipline = input("Please enter discipline's name:")
        studentID = UI.readPositiveInteger("Please enter the student's ID: ")
        try:
            self.__graCtrl.removeStudentFromDiscipline(discipline, studentID)
        except (DisciplineException, StudentException, GradeException) as ex:
            print(ex)
                
    def __showAllGrades(self):
        '''
        displays all Grades
        Input: -
        Output: a list of all Grades
        '''
        gras = self.__graCtrl.getAll()
        if len(gras) == 0:
            print("There are no grades in the register.")
        else:
            for e in gras:
                print(e)
            
    def gradeMenu(self):
        commandDict = {'1': self.__addStudentToDiscipline,
                       '2': self.__updateGrade,
                       '3': self.__removeStudentFromDiscipline,
                       '4': self.__showAllGrades}
        while True:
            UI.printGradeMenu()
            command = input("Please enter your command: ")
            while not UI.validInputStudentCommand(command):
                print("Please enter a valid command!")
                command = input("Please enter your command: ")
            if command == '0':
                return
            commandDict[command]()
    
    def __byDiscipline(self):
        '''
        displays all students and grades at a given discipline
        Input: -
        Output: all students and grades at a given discipline
        '''
        disciplineName = input("Please enter the Discipline name: ")
        try:
            res = self.__staCtrl.byDiscipline(disciplineName)
            if res == []:
                print("There are no students added to the given discipline.")
            else:
                for x in res:
                    print(x)
        except DisciplineException as e:
            print(e)
        
    def __alphabeticallyByDiscipline(self):
        '''
        displays alphabetically all students and grades at a given discipline
        Input: -
        Output: all students and grades at a given discipline sorted alphabetically
        '''
        disciplineName = input("Please enter the Discipline name: ")
        try:
            res = self.__staCtrl.alphabeticallyByDiscipline(disciplineName)
            if res == []:
                print("There are no students added to the given discipline.")
            else:
                for x in res:
                    print(x)
        except DisciplineException as e:
            print(e)
    
    def __byGradeByDiscipline(self):
        '''
        displays by grade all students and grades at a given discipline
        Input: -
        Output: all students and grades at a given discipline sorted by grade
        '''
        disciplineName = input("Please enter the Discipline name: ")
        try:
            res = self.__staCtrl.byGradeByDiscipline(disciplineName)
            if res == []:
                print("There are no students added to the given discipline.")
            else:
                for x in res:
                    print(x)
        except DisciplineException as e:
            print(e)
    
    def __byAverageGrades(self):
        '''
        displays by the average grade all students and grades
        Input: -
        Output: all students and grades sorted by the average grade
        '''
        res = self.__staCtrl.byAverageGrades()
        if res == []:
            print("There are no students added to the given discipline.")
        else:
            for x in res:
                print(x)

    def statisticsMenu(self):
        commandDict = {'1': self.__byDiscipline,
                       '2': self.__alphabeticallyByDiscipline,
                       '3': self.__byGradeByDiscipline,
                       '4': self.__byAverageGrades}
        while True:
            UI.printStatisticsMenu()
            command = input("Please enter your command: ")
            while not UI.validInputStudentCommand(command):
                print("Please enter a valid command!")
                command = input("Please enter your command: ")
            if command == '0':
                return
            commandDict[command]()
            
    def undoMenu(self):
        res = self.__undoCtrl.undo()
        if res == True:
            print("Undo successfully made.")
        else:
            print("No undo operations are possible.")
            
    def redoMenu(self):
        res = self.__undoCtrl.redo()
        if res == True:
            print("Redo successfully made.")
        else:
            print("No redo operations are possible.")
            
    def mainMenu(self):
        commandDict = {'1': self.disciplineMenu,
                       '2': self.studentMenu,
                       '3': self.gradeMenu,
                       '4': self.statisticsMenu,
                       '5': self.undoMenu,
                       '6': self.redoMenu}
        while True:
            UI.printMenu()
            command = input("Please enter your command: ")
            while not UI.validInputCommand(command):
                print("Please enter a valid command!")
                command = input("Please enter your command: ")
            if command == '0':
                return
            commandDict[command]()
