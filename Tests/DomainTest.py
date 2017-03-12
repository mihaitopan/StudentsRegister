import unittest
from Domain.Discipline import Discipline
from Domain.Grade import Grade
from Domain.Student import Student

class DisciplineDomainTestCase(unittest.TestCase):
    '''
    unit test for DisciplineDomain
    '''
    def setUp(self):
        self.dis = Discipline("maths", "Andrea")
    
    def testGetters(self):
        self.assertEqual(self.dis.getName(), "maths")
        self.assertEqual(self.dis.getTeacher(), "Andrea")
        
    def testSetters(self):
        self.dis.setName("physics")
        self.dis.setTeacher("Corega")
        
        self.assertEqual(self.dis.getName(), "physics")
        self.assertEqual(self.dis.getTeacher(), "Corega")
        
class GradeDomainTestCase(unittest.TestCase):
    '''
    unit test for GradeDomain
    '''
    def setUp(self):
        self.gra = Grade("maths", 1, 8)
    
    def testGetters(self):
        self.assertEqual(self.gra.getDiscipline(), "maths")
        self.assertEqual(self.gra.getStudentID(), 1)
        self.assertEqual(self.gra.getGrade(), 8)
        
    def testSetters(self):
        self.gra.setDiscipline("physics")
        self.gra.setStudentID(2)
        self.gra.setGrade(9)
        
        self.assertEqual(self.gra.getDiscipline(), "physics")
        self.assertEqual(self.gra.getStudentID(), 2)
        self.assertEqual(self.gra.getGrade(), 9)
        
class StudentDomainTestCase(unittest.TestCase):
    '''
    unit test for StudentDomain
    '''
    def setUp(self):
        self.stu = Student(1, "John")
    
    def testGetters(self):
        self.assertEqual(self.stu.getID(), 1)
        self.assertEqual(self.stu.getName(), "John")
        
    def testSetters(self):
        self.stu.setID(2)
        self.stu.setName("Mike")
        
        self.assertEqual(self.stu.getID(), 2)
        self.assertEqual(self.stu.getName(), "Mike")
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
