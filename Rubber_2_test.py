from Runner_2 import *
import unittest

class TournamentTest(unittest.TestCase):

    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner("Усэйн", 10)
        self.runner_2 = Runner("Андрей", 9)
        self.runner_3 = Runner("Ник", 3)

    def tearDownClass(cls):
        print(cls.all_results)

    def test_tourne1(self):
        self.distan = 90
        tourne_1 = Tournament(self.distan, (self.runner_1, self.runner_3))
        tourne_1.start()

    def test_tourne2(self):
        tourne_2 = Tournament(self.distan, (self.runner_2, self.runner_3))
        tourne_2.start()

    def test_tourne3(self):
        tourne_3 = Tournament(self.distan, (self.runner_1, self.runner_2, self.runner_3))
        tourne_3.start()