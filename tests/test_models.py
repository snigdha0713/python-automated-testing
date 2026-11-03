"""Unit tests for student record validation and calculated results."""

import unittest
from student_records import InvalidStudentError, StudentRecord

class StudentRecordTests(unittest.TestCase):
    def test_record_strips_id_and_name(self):
        student = StudentRecord(" S001 ", " Asha Sen ", [80, 90])
        self.assertEqual(student.student_id, "S001")
        self.assertEqual(student.name, "Asha Sen")

    def test_marks_are_stored_as_an_immutable_tuple(self):
        marks = [80, 90]
        student = StudentRecord("S001", "Asha", marks)
        marks.append(100)
        self.assertEqual(student.marks, (80, 90))

    def test_average_is_calculated_correctly(self):
        self.assertEqual(StudentRecord("S001", "Asha", [80, 90, 100]).average, 90)

    def test_grade_for_each_boundary(self):
        cases = [([90], "A"), ([89], "B"), ([75], "B"), ([74], "C"), ([60], "C"), ([59], "D"), ([40], "D"), ([39], "F"), ([0], "F")]
        for marks, expected in cases:
            with self.subTest(marks=marks):
                self.assertEqual(StudentRecord("S1", "Test", marks).grade, expected)

    def test_empty_id_is_rejected(self):
        with self.assertRaises(InvalidStudentError): StudentRecord(" ", "Asha", [80])

    def test_empty_name_is_rejected(self):
        with self.assertRaises(InvalidStudentError): StudentRecord("S001", " ", [80])

    def test_empty_marks_are_rejected(self):
        with self.assertRaises(InvalidStudentError): StudentRecord("S001", "Asha", [])

    def test_mark_below_zero_is_rejected(self):
        with self.assertRaises(InvalidStudentError): StudentRecord("S001", "Asha", [-1])

    def test_mark_above_100_is_rejected(self):
        with self.assertRaises(InvalidStudentError): StudentRecord("S001", "Asha", [101])

    def test_non_integer_mark_is_rejected(self):
        with self.assertRaises(InvalidStudentError): StudentRecord("S001", "Asha", [80.5])

    def test_boolean_mark_is_rejected(self):
        with self.assertRaises(InvalidStudentError): StudentRecord("S001", "Asha", [True])

if __name__ == "__main__":
    unittest.main()
