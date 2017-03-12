class DisciplineException(Exception):
    def __init__(self, msg):
        self.__message = msg
    
    def __str__(self):
        return self.__message
    
class StudentException(Exception):
    def __init__(self, msg):
        self.__message = msg
    
    def __str__(self):
        return self.__message
    
class GradeException(Exception):
    def __init__(self, msg):
        self.__message = msg
    
    def __str__(self):
        return self.__message