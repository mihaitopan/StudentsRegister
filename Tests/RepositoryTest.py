import unittest
from Domain.Discipline import Discipline
from Domain.Exceptions import DisciplineException
from Repository.DisciplineRepository import DisciplineRepository
from Domain.Student import Student
from Domain.Exceptions import StudentException
from Repository.StudentRepository import StudentRepository

class DisciplineRepositoryTestCase(unittest.TestCase):
    '''
    unit test for DisciplineRepository
    '''
    def setUp(self):
        self.repo = DisciplineRepository()
        
        d1 = Discipline("maths", "Andrea")
        d2 = Discipline("physics", "Columban")
        
        self.repo.add(d1)
        self.repo.add(d2)
        
    def testAdd(self):
        d = Discipline("chemistry", "Baiazid")
        self.repo.add(d)
        self.assertEqual(len(self.repo), 3)
        
        self.assertRaises(DisciplineException, self.repo.add, d)
        
    def testFindByName(self):
        d = self.repo.findByName("maths")
        self.assertEqual(d, Discipline("maths", "Andrea"))

        d = self.repo.findByName("js")
        self.assertEqual(d, None)
        self.assertTrue(d == None)

    def testUpdate(self):
        upD = Discipline("physics", "Huber")
        self.repo.update("physics","Huber")
        d = self.repo.findByName("physics")
        self.assertEqual(d, upD)

    def testRemove(self):
        self.repo.remove("maths")
        self.assertEqual(len(self.repo), 1)

        self.assertRaises(DisciplineException, self.repo.remove, "chemistry")
        
class StudentRepositoryTestCase(unittest.TestCase):
    '''
    unit test for StudentRepository
    '''
    def setUp(self):
        self.repo = StudentRepository()
        
        s1 = Student(1, "1")
        s2 = Student(2, "2")
        
        self.repo.add(s1)
        self.repo.add(s2)
        
    def testAdd(self):
        s = Student(3, "3")
        self.repo.add(s)
        self.assertEqual(len(self.repo), 3)
        
        self.assertRaises(StudentException, self.repo.add, s)
        
    def testFindByID(self):
        s = self.repo.findByID(1)
        self.assertEqual(s, Student(1, "1"))

        s = self.repo.findByID(169)
        self.assertEqual(s, None)
        self.assertTrue(s == None)

    def testUpdate(self):
        upS = Student(2, "8")
        self.repo.update(2,"8")
        s = self.repo.findByID(2)
        self.assertEqual(s, upS)

    def testRemove(self):
        self.repo.remove(1)
        self.assertEqual(len(self.repo), 1)

        self.assertRaises(StudentException, self.repo.remove, 1)

if __name__ == '__main__':
    unittest.main(verbosity=2)

