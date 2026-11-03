# Student Records Management - Automated Testing

A small Python module for managing student records and calculating academic results. It demonstrates unit testing, integration testing, input validation, and a test-first development approach.

## Features

- Add, retrieve, search, update, and delete student records.
- Calculate an individual student's average and grade.
- Produce a class summary with student count, class average, and top student.
- Validate input and report clear errors.

The project uses an in-memory repository. It needs no external database or dataset.

## Requirements

- Python 3.10 or newer
- No third-party packages

## Project structure

    student_records/
        __init__.py
        exceptions.py
        manager.py
        models.py
        repository.py
    tests/
        __init__.py
        test_integration.py
        test_manager.py
        test_models.py
        test_repository.py
    documentation/
        TESTING_REPORT.md
    README.md
    requirements.txt
    .gitignore

## Run the tests

From the repository root:

    python -m unittest discover -s tests -v

The suite contains 34 test methods across model, repository, manager, and integration groups. Grade-boundary cases are also checked using subtests.

## Use the module

    from student_records import (
        StudentRecord,
        StudentManager,
        InMemoryStudentRepository,
    )

    repository = InMemoryStudentRepository()
    manager = StudentManager(repository)

    student = StudentRecord("S001", "Asha", [85, 91, 78])
    manager.add_student(student)

    print(manager.get_student("S001"))
    print(manager.get_student_average("S001"))
    print(manager.get_student_grade("S001"))
    print(manager.get_class_summary())

The grade scale is a project example: A = 90-100, B = 75-89, C = 60-74, D = 40-59, F = 0-39. It is not an institutional grading policy.

## Design

- `models.py` validates student details and calculates average and grade.
- `repository.py` stores records and provides add, get, list, update, delete, and search operations.
- `manager.py` coordinates operations and calculates class summaries.
- `exceptions.py` defines clear errors for invalid records, duplicate IDs, and missing students.

The separation makes each part easier to test independently. Student records are immutable; updates create replacement records.

## Testing approach

Model tests cover validation and calculations. Repository tests cover storage operations. Manager tests cover business operations and error handling. Integration tests run a complete workflow using the manager and repository together.

The test methodology, test inventory, and reasons for each test group are described in `documentation/TESTING_REPORT.md`.

## Verification

The test suite was executed in the development environment using Python's built-in `unittest` framework: 34 tests passed, 0 failures, 0 errors.

All project files are included in this repository. No proprietary resources or external datasets are required.
