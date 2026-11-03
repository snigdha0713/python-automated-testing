"""Student data model and academic result helpers."""

from dataclasses import dataclass
from statistics import mean

from .exceptions import InvalidStudentError


@dataclass(frozen=True, slots=True)
class StudentRecord:
    """Store a student's ID, name, and assessment marks.

    Records are immutable. Updates create a replacement record so callers
    cannot unexpectedly change values held by the repository.
    """

    student_id: str
    name: str
    marks: tuple[int, ...]

    def __init__(self, student_id: str, name: str, marks: list[int] | tuple[int, ...]):
        clean_id = student_id.strip() if isinstance(student_id, str) else ""
        clean_name = name.strip() if isinstance(name, str) else ""

        if not clean_id:
            raise InvalidStudentError("Student ID cannot be empty.")
        if not clean_name:
            raise InvalidStudentError("Student name cannot be empty.")
        if not isinstance(marks, (list, tuple)) or not marks:
            raise InvalidStudentError("At least one mark is required.")

        validated_marks: list[int] = []
        for mark in marks:
            if type(mark) is not int:
                raise InvalidStudentError("Every mark must be a whole number.")
            if not 0 <= mark <= 100:
                raise InvalidStudentError("Marks must be between 0 and 100.")
            validated_marks.append(mark)

        object.__setattr__(self, "student_id", clean_id)
        object.__setattr__(self, "name", clean_name)
        object.__setattr__(self, "marks", tuple(validated_marks))

    @property
    def average(self) -> float:
        """Return the arithmetic mean of the student's marks."""
        return mean(self.marks)

    @property
    def grade(self) -> str:
        """Return the project's example grade for the student's average."""
        average = self.average
        if average >= 90:
            return "A"
        if average >= 75:
            return "B"
        if average >= 60:
            return "C"
        if average >= 40:
            return "D"
        return "F"
