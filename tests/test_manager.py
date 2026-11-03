"""Unit tests for student manager business operations."""

import unittest
from student_records import InMemoryStudentRepository, StudentManager, StudentNotFoundError, StudentRecord

class StudentManagerTests(unittest.TestCase):
    def setUp(self):
        self.manager = StudentManager(InMemoryStudentRepository())
        self.manager.add_student(StudentRecord("S001", "Asha", [80, 90]))
        self.manager.add_student(StudentRecord("S002", "Ravi", [70, 75]))

    def test_add_and_list_students(self): self.assertEqual(len(self.manager.list_students()), 2)
    def test_get_student_strips_id_whitespace(self): self.assertEqual(self.manager.get_student(" S001 ").name, "Asha")

    def test_update_student_replaces_name_and_marks(self):
        updated = self.manager.update_student("S001", name="Asha Sen", marks=[95, 97])
        self.assertEqual(updated.name, "Asha Sen")
        self.assertEqual(self.manager.get_student("S001").marks, (95, 97))

    def test_update_missing_student_raises_error(self):
        with self.assertRaises(StudentNotFoundError): self.manager.update_student("S999", name="Missing", marks=[50])

    def test_remove_student(self):
        removed = self.manager.remove_student("S002")
        self.assertEqual(removed.name, "Ravi")
        self.assertEqual(len(self.manager.list_students()), 1)

    def test_search_students_by_partial_name(self): self.assertEqual([s.student_id for s in self.manager.search_students("ash")], ["S001"])
    def test_student_average_and_grade(self):
        self.assertEqual(self.manager.get_student_average("S001"), 85)
        self.assertEqual(self.manager.get_student_grade("S001"), "B")

    def test_empty_student_id_is_rejected(self):
        with self.assertRaises(ValueError): self.manager.get_student("   ")

    def test_class_summary(self):
        summary = self.manager.get_class_summary()
        self.assertEqual(summary["student_count"], 2)
        self.assertEqual(summary["class_average"], 78.75)
        self.assertEqual(summary["top_student"].student_id, "S001")

    def test_empty_class_summary(self):
        empty = StudentManager(InMemoryStudentRepository())
        self.assertEqual(empty.get_class_summary(), {"student_count": 0, "class_average": None, "top_student": None})

if __name__ == "__main__": unittest.main()
