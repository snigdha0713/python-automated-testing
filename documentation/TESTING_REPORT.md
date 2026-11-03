# Testing Report - Student Records Management

## 1. Project overview

This project is a small Python module for maintaining student records. It supports adding, retrieving, listing, searching, updating, and deleting students. It also calculates individual averages and grades, and prepares a class summary.

The data is held in an in-memory repository. This keeps the exercise self-contained: no database, network connection, proprietary service, or external dataset is needed.

## 2. Development methodology

The project follows a test-first approach at the feature level. The expected rules and edge cases were identified first, and tests were written to describe these requirements before the related implementation was finalised. The module was then implemented and the full suite was run. The GitHub commit history records the source and test additions; it does not claim that each individual test file was committed before every production-code line.

## 3. Module design

- `models.py`: validates student IDs, names, and marks; calculates average and grade.
- `repository.py`: stores records and provides create, read, update, delete, and search operations.
- `manager.py`: coordinates application operations and prepares class summaries.
- `exceptions.py`: defines specific exceptions for invalid records, duplicate IDs, and missing students.

Student records are immutable. An update creates a replacement record, so callers cannot change an object stored by the repository without using the manager.

## 4. Test cases and why they are included

### Model unit tests (`tests/test_models.py`)

| Test | Purpose |
|---|---|
| Strip ID and name | Ensures surrounding spaces are removed. |
| Immutable marks | Confirms changing the original input list does not alter the record. |
| Average calculation | Checks the mean of several marks. |
| Grade boundaries | Checks values at the edges of each grade band. |
| Empty ID, name, or marks | Rejects incomplete student information. |
| Marks outside 0-100 | Enforces the valid mark range. |
| Non-integer and boolean marks | Prevents invalid values from being treated as marks. |

### Repository unit tests (`tests/test_repository.py`)

| Test | Purpose |
|---|---|
| Add and get | Checks that a stored student can be retrieved. |
| Duplicate ID | Ensures an existing record is not overwritten. |
| Copy of list | Confirms callers cannot clear the repository by clearing a returned list. |
| Update existing record | Checks replacement of a student record. |
| Update missing record | Checks the specific missing-student error. |
| Delete existing record | Confirms deletion returns the removed record. |
| Get/delete missing record | Checks errors for unknown IDs. |
| Case-insensitive search | Makes name lookup convenient. |
| Blank search | Returns no results for a query with no useful text. |

### Manager unit tests (`tests/test_manager.py`)

These tests cover add/list, ID whitespace, updates, missing IDs, removal, search, individual average and grade, class summary, empty class summary, and blank IDs. They check the application-facing operations rather than the internal dictionary implementation.

### Integration tests (`tests/test_integration.py`)

The workflow test adds two students, searches for a student, updates a record, calculates a class summary, and removes a student. Other tests confirm a duplicate ID does not replace an existing student and an invalid update leaves the original record unchanged.

## 5. Running the tests

Python 3.10 or newer is recommended. No third-party packages are required.

From the project root, run:

    python -m unittest discover -s tests -v

The tests create fresh in-memory repositories, so results do not depend on previous runs or external data.

## 6. Refactoring and maintainability

The project separates validation, data storage, and business operations. Specific exceptions make error cases clear. Immutable records make updates explicit. Tests are grouped by responsibility so a failure is easier to locate.

The grade boundaries are example rules for this exercise: A = 90-100, B = 75-89, C = 60-74, D = 40-59, and F = 0-39. They should be changed if a real institution uses a different scale.

## 7. Test execution record

Command executed:

    python -m unittest discover -s tests -v

Result in the development environment: **34 tests passed, 0 failures, 0 errors.** The suite was run after the module and test files were assembled.

## 8. Conclusion

The test suite checks normal operations, validation rules, edge cases, and error conditions across the model, repository, and manager. Integration tests check that the separate parts work together as one workflow. The project uses only Python's standard library and is self-contained.
