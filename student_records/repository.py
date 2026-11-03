"""In-memory storage for student records."""

from .exceptions import DuplicateStudentError, StudentNotFoundError
from .models import StudentRecord


class InMemoryStudentRepository:
    """Store records in a dictionary keyed by student ID."""

    def __init__(self) -> None:
        self._students: dict[str, StudentRecord] = {}

    def add(self, student: StudentRecord) -> None:
        """Add a record, rejecting an ID that already exists."""
        if student.student_id in self._students:
            raise DuplicateStudentError(
                f"Student ID '{student.student_id}' already exists."
            )
        self._students[student.student_id] = student

    def get(self, student_id: str) -> StudentRecord:
        """Return one record or raise StudentNotFoundError."""
        try:
            return self._students[student_id]
        except KeyError as exc:
            raise StudentNotFoundError(
                f"No student found with ID '{student_id}'."
            ) from exc

    def list_all(self) -> list[StudentRecord]:
        """Return records in insertion order."""
        return list(self._students.values())

    def update(self, student: StudentRecord) -> None:
        """Replace an existing student record."""
        if student.student_id not in self._students:
            raise StudentNotFoundError(
                f"No student found with ID '{student.student_id}'."
            )
        self._students[student.student_id] = student

    def delete(self, student_id: str) -> StudentRecord:
        """Remove and return a record."""
        try:
            return self._students.pop(student_id)
        except KeyError as exc:
            raise StudentNotFoundError(
                f"No student found with ID '{student_id}'."
            ) from exc

    def search_by_name(self, query: str) -> list[StudentRecord]:
        """Return records whose names contain the query, ignoring case."""
        normalized_query = query.strip().casefold()
        if not normalized_query:
            return []
        return [
            student
            for student in self._students.values()
            if normalized_query in student.name.casefold()
        ]
