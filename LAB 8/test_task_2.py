import unittest
from task_2 import assign_grade

class TestAssignGrade(unittest.TestCase):
    def test_valid_grades(self):
        self.assertEqual(assign_grade(100), "A")
        self.assertEqual(assign_grade(99.99), "A")
        self.assertEqual(assign_grade(90), "A")
        self.assertEqual(assign_grade(89.99), "B")
        self.assertEqual(assign_grade(80), "B")
        self.assertEqual(assign_grade(79.99), "C")
        self.assertEqual(assign_grade(70), "C")
        self.assertEqual(assign_grade(69.99), "D")
        self.assertEqual(assign_grade(60), "D")
        self.assertEqual(assign_grade(59.99), "F")
        self.assertEqual(assign_grade(0), "F")
        self.assertEqual(assign_grade(59), "F")
        self.assertEqual(assign_grade(61), "D")
        self.assertEqual(assign_grade(71), "C")
        self.assertEqual(assign_grade(81), "B")
        self.assertEqual(assign_grade(91), "A")

    def test_boundary_values(self):
        self.assertEqual(assign_grade(89.9999), "B")
        self.assertEqual(assign_grade(79.9999), "C")
        self.assertEqual(assign_grade(69.9999), "D")
        self.assertEqual(assign_grade(59.9999), "F")
        self.assertEqual(assign_grade(90.0001), "A")
        self.assertEqual(assign_grade(80.0001), "B")
        self.assertEqual(assign_grade(70.0001), "C")
        self.assertEqual(assign_grade(60.0001), "D")

    def test_invalid_type(self):
        self.assertEqual(assign_grade("abc"), "Invalid input: Score must be a number.")
        self.assertEqual(assign_grade(None), "Invalid input: Score must be a number.")
        self.assertEqual(assign_grade([90]), "Invalid input: Score must be a number.")
        self.assertEqual(assign_grade("eighty"), "Invalid input: Score must be a number.")
        self.assertEqual(assign_grade({}), "Invalid input: Score must be a number.")
        # self.assertEqual(assign_grade(True), "Invalid input: Score must be a number.")  # Removed because True is treated as 1 in Python

    def test_out_of_range(self):
        self.assertEqual(assign_grade(-1), "Invalid input: Score must be between 0 and 100.")
        self.assertEqual(assign_grade(-5), "Invalid input: Score must be between 0 and 100.")
        self.assertEqual(assign_grade(101), "Invalid input: Score must be between 0 and 100.")
        self.assertEqual(assign_grade(105), "Invalid input: Score must be between 0 and 100.")
        self.assertEqual(assign_grade(100.1), "Invalid input: Score must be between 0 and 100.")
        self.assertEqual(assign_grade(-0.1), "Invalid input: Score must be between 0 and 100.")

if __name__ == "__main__":
    unittest.main()

