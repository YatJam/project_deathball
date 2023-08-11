import unittest
from models.team import Team

class TestTeam(unittest.TestCase):

    def setUp(self):
        self.team1 = Team("Jumpy Jumpers", "Elves", 14, 2, 28)
        self.team2 = Team("Reddy Reds", "Orcs", 32, 1, 104)
        self.team3 = Team("Bluey Blues", "Orcs", None, None, 104)
   

    def test_room_has_name(self):
        self.assertEqual("Jumpy Jumpers", self.team1.name)

    def test_return_zero_value_from_None_values(self):
        self.assertEqual(0, self.team3.total_points())
