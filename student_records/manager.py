"""Application services for managing student records."""

from .models import StudentRecord
from .repository import InMemoryStudentRepository

class StudentManager:
    """Apply student-management rules using a repository."""
    def __init__(self, repository: InMemoryStudentRepository) -> None:
        self._repository = repository

    def add_student(self, student: StudentRecord) -> None:
        self._repository.add(student)

    def get_student(self, student_id: str) -> StudentRecord:
        return self._repository.get(self._validate_id(student_id))

    def list_students(self) -> list[StudentRecord]:
        return self._repository.list_all()

    def update_student(self, student_id: str, *, name: str, marks: list[int] | tuple[int, ...]) -> StudentRecord:
        clean_id = self._validate_id(student_id)
        updated = StudentRecord(clean_id, name, marks)
        self._repository.update(updated)
        return updated

    def remove_student(self, student_id: str) -> StudentRecord:
        return self._repository.delete(self._validate_id(student_id))

    def search_students(self, query: str) -> list[StudentRecord]:
        if not isinstance(query, str):
            raise ValueError("Search text must be a string.")
        return self._repository.search_by_name(query)

    def get_student_average(self, student_id: str) -> float:
        return self.get_student(student_id).average

    def get_student_grade(self, student_id: str) -> str:
        return self.get_student(student_id).grade

    def get_class_summary(self) -> dict[str, object]:
        students = self.list_students()
        if not students:
            return {"student_count": 0, "class_average": None, "top_student": None}
        class_average = sum(student.average for student in students) / len(students)
        top_student = max(students, key=lambda student: student.average)
        return {"student_count": len(students), "class_average": class_average, "top_student": top_student}

    @staticmethod
    def _validate_id(student_id: str) -> str:
        if not isinstance(student_id, str) or not student_id.strip():
            raise ValueError("Student ID cannot be empty.")
        return student_id.strip()
