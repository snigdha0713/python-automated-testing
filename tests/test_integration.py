"""Integration tests for complete student record workflows."""

import unittest
from student_records import DuplicateStudentError, InMemoryStudentRepository, StudentManager, StudentRecord

class StudentWorkflowIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.repository = InMemoryStudentRepository()
        self.manager = StudentManager(self.repository)

    def test_add_search_update_summary_and_delete_workflow(self):
        self.manager.add_student(StudentRecord("S001", "Asha", [80, 90]))
        self.manager.add_student(StudentRecord("S002", "Ravi", [70, 75]))
        self.assertEqual([s.student_id for s in self.manager.search_students("ash")], ["S001"])
        self.manager.update_student("S001", name="Asha Sen", marks=[95, 97])
        summary = self.manager.get_class_summary()
        self.assertEqual(summary["student_count"], 2)
        self.assertAlmostEqual(summary["class_average"], 84.25)
        self.assertEqual(summary["top_student"].name, "Asha Sen")
        self.assertEqual(self.manager.remove_student("S002").student_id, "S002")
        self.assertEqual([s.student_id for s in self.manager.list_students()], ["S001"])

    def test_duplicate_id_does_not_replace_original_record(self):
        original = StudentRecord("S001", "Asha", [80])
        self.manager.add_student(original)
        with self.assertRaises(DuplicateStudentError): self.manager.add_student(StudentRecord("S001", "Other", [99]))
        self.assertEqual(self.manager.get_student("S001"), original)

    def test_invalid_update_does_not_change_existing_record(self):
        original = StudentRecord("S001", "Asha", [80])
        self.manager.add_student(original)
        with self.assertRaises(ValueError): self.manager.update_student("S001", name="Asha", marks=[120])
        self.assertEqual(self.manager.get_student("S001"), original)

if __name__ == "__main__": unittest.main()
