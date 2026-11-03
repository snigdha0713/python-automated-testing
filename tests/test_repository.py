"""Unit tests for the in-memory student repository."""

import unittest
from student_records import DuplicateStudentError, InMemoryStudentRepository, StudentNotFoundError, StudentRecord

class RepositoryTests(unittest.TestCase):
    def setUp(self):
        self.repository = InMemoryStudentRepository()
        self.asha = StudentRecord("S001", "Asha", [80, 90])

    def test_add_and_get_student(self):
        self.repository.add(self.asha)
        self.assertEqual(self.repository.get("S001"), self.asha)

    def test_duplicate_student_id_is_rejected(self):
        self.repository.add(self.asha)
        with self.assertRaises(DuplicateStudentError): self.repository.add(self.asha)

    def test_list_all_returns_a_new_list(self):
        self.repository.add(self.asha)
        result = self.repository.list_all()
        result.clear()
        self.assertEqual(self.repository.list_all(), [self.asha])

    def test_update_existing_student(self):
        self.repository.add(self.asha)
        updated = StudentRecord("S001", "Asha Das", [95])
        self.repository.update(updated)
        self.assertEqual(self.repository.get("S001"), updated)

    def test_update_missing_student_is_rejected(self):
        with self.assertRaises(StudentNotFoundError): self.repository.update(StudentRecord("S999", "Nobody", [50]))

    def test_delete_returns_removed_student(self):
        self.repository.add(self.asha)
        self.assertEqual(self.repository.delete("S001"), self.asha)
        self.assertEqual(self.repository.list_all(), [])

    def test_get_missing_student_is_rejected(self):
        with self.assertRaises(StudentNotFoundError): self.repository.get("S999")

    def test_delete_missing_student_is_rejected(self):
        with self.assertRaises(StudentNotFoundError): self.repository.delete("S999")

    def test_search_is_case_insensitive(self):
        self.repository.add(self.asha)
        self.assertEqual(self.repository.search_by_name("ASHA"), [self.asha])

    def test_blank_search_returns_no_results(self):
        self.repository.add(self.asha)
        self.assertEqual(self.repository.search_by_name("   "), [])

if __name__ == "__main__":
    unittest.main()
