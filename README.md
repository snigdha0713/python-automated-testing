# Student Records Management - Automated Testing

A small Python module for managing student records and calculating academic results. The project demonstrates unit testing, integration testing, input validation, and a test-first development workflow.

## Features

- Add a student record with a unique ID, name, and marks.
- Retrieve, search, update, and delete student records.
- Calculate an individual student's average and grade.
- Produce a class summary with student count, class average, and top student.
- Validate input and report clear errors for invalid operations.

The project uses an in-memory repository, so no external database or dataset is required.

## Requirements

- Python 3.10 or newer
- No third-party packages

Check Python with:

    python --version

## Project structure

    python-automated-testing/
    ├── student_records/
    │   ├── __init__.py
    │   ├── exceptions.py
    │   ├── models.py
    │   ├── repository.py
    │   └── manager.py
    ├── tests/
    │   ├── __init__.py
    │   ├── test_models.py
    │   ├── test_repository.py
    │   ├── test_manager.py
    │   └── test_integration.py
    ├── documentation/
    │   └── TESTING_REPORT.md
    ├── README.md
    ├── requirements.txt
    └── .gitignore

## Run the test suite

Run from the repository root:

    python -m unittest discover -s tests -v

The tests use fresh in-memory repositories and do not need a database, network connection, or external files.

## Use the module

    from student_records import StudentRecord, StudentManager, InMemoryStudentRepository

    repository = InMemoryStudentRepository()
    manager = StudentManager(repository)

    student = StudentRecord(student_id="S001", name="Asha", marks=[85, 91, 78])
    manager.add_student(student)

    print(manager.get_student("S001"))
    print(manager.get_student_average("S001"))
    print(manager.get_student_grade("S001"))
    print(manager.get_class_summary())

The grade scale used in this exercise is: A = 90-100, B = 75-89, C = 60-74, D = 40-59, and F = 0-39. These are project-defined example boundaries, not an institutional grading policy.

## Design

The project separates data validation, storage, and application operations:

- `models.py` defines a student record and validates its values.
- `repository.py` provides an in-memory store with CRUD operations.
- `manager.py` coordinates student operations and calculates results.
- `exceptions.py` contains specific exceptions for invalid data and missing students.

This separation makes the model and business rules testable without relying on a user interface or database.

## Testing approach

Tests are grouped by responsibility:

- Model unit tests check validation and calculated values.
- Repository unit tests check storage operations and duplicate IDs.
- Manager unit tests check business rules and error handling.
- Integration tests exercise a complete workflow across the manager and repository.

The development notes in `documentation/TESTING_REPORT.md` describe the test-first method, each test group, edge cases, and how to run the suite.

## Test result

The test suite was run in the development environment with Python's built-in `unittest` framework: **34 tests passed**.

## Notes

All required source code, tests, and documentation are included in this repository. The application has no third-party dependencies.
