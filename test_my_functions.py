import unittest
import my_functions
from unittest.mock import patch

class Test_my_functions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('lol1')

    @classmethod
    def tearDownClass(cls):
        print('lol2')

    def setUp(self):
        print('setup')
        self.person = my_functions.Sim('blond')

    def tearDown(self):
        pass

    def test_pole(self):
        self.assertEqual(my_functions.pole(2), 4)

    def test_przefarbuj(self):
        self.person.przefarbuj('czarny')
        self.person.wlosy = 'czarny'
        self.assertEqual(self.person.wlosy, 'czarny')

    def test_division(self):
        self.assertEqual(my_functions.division(15, 3), 5)
        #a gdy chce sprawdzić czy zwraca odpowiednie błędy
        self.assertRaises(ValueError, my_functions.division, 23, 0)
        #lub tak
        with self.assertRaises(ValueError):
            my_functions.division(10, 0)



#konsola: python -m unittest test_my_functions.py lub

if __name__ == '__main__':
    unittest.main()