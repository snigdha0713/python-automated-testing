"""Exceptions raised by the student records module."""


class InvalidStudentError(ValueError):
    """Raised when a student record contains invalid data."""


class DuplicateStudentError(ValueError):
    """Raised when a student ID is already present."""


class StudentNotFoundError(LookupError):
    """Raised when a requested student does not exist."""
