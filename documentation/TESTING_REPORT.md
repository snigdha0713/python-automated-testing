# Testing Report - Student Records Management

## 1. Project overview
This project is a small Python module for maintaining student records. It supports adding, retrieving, listing, searching, updating, and deleting students. It also calculates individual averages and grades, and prepares a class summary.

The data is held in an in-memory repository. This keeps the project self-contained: no database, network connection, proprietary service, or external dataset is needed.

## 2. Development methodology
The module was developed first, and the automated tests were added after the main functionality was in place. This is one of the approaches allowed by the assignment. The tests were then used to check the expected behaviour, exercise edge cases, and verify that the components worked together.

The project therefore documents a test-after-development approach. It does not claim to have followed a strict red-green-refactor TDD cycle.

## 3. Module design
- `models.py`: validates student IDs, names, and marks; calculates average and grade.
- `repository.py`: stores records and provides add, get, list, update, delete, and search operations.
- `manager.py`: coordinates application operations and prepares class summaries.
- `exceptions.py`: defines specific exceptions for invalid records, duplicate IDs, and missing students.

Student records are immutable. An update creates a replacement record, so callers cannot change an object stored by the repository without using the manager.

## 4. Test cases and why they are included

### Model unit tests - `tests/test_models.py`
| Test case | Why it is included |
|---|---|
| Strip ID and name | Ensures surrounding spaces are removed. |
| Immutable marks | Confirms changing the original input list does not change the stored record. |
| Average calculation | Checks the arithmetic mean of multiple marks. |
| Grade boundaries | Checks values at the edge of each grade band. |
| Empty ID, name, or marks | Rejects incomplete student information. |
| Marks below 0 or above 100 | Enforces the valid mark range. |
| Non-integer and boolean marks | Prevents invalid values from being treated as marks. |

### Repository unit tests - `tests/test_repository.py`
| Test case | Why it is included |
|---|---|
| Add and get | Checks that a stored student can be retrieved. |
| Duplicate ID | Ensures an existing record is not overwritten. |
| Copy of list | Ensures callers cannot clear the repository by clearing a returned list. |
| Update existing record | Checks replacement of an existing record. |
| Update missing record | Checks the specific missing-student error. |
| Delete existing record | Confirms deletion returns the removed record. |
| Get/delete missing record | Checks errors for unknown IDs. |
| Case-insensitive search | Makes name lookup convenient. |
| Blank search | Returns no results for a query with no useful text. |

### Manager unit tests - `tests/test_manager.py`
These tests cover adding and listing students, trimming ID whitespace, updating details, handling missing IDs, removing records, searching names, calculating individual averages and grades, producing a class summary, handling an empty class, and rejecting blank IDs. They test application-facing operations rather than the internal dictionary implementation.

### Integration tests - `tests/test_integration.py`
The main workflow test adds two students, searches for one, updates a record, calculates the class summary, and removes a student. Other tests confirm that a duplicate ID does not replace an existing student and that an invalid update leaves the original record unchanged.

## 5. Running the tests
Python 3.10 or newer is recommended. No third-party packages are required.

From the project root, run:
```bash
python -m unittest discover -s tests -v
```
The tests create fresh in-memory repositories, so results do not depend on previous runs or external data.

## 6. Refactoring and maintainability
The project separates validation, data storage, and business operations. Specific exceptions make error cases clear. Immutable records make updates explicit. Tests are grouped by responsibility so a failure is easier to locate.

The grade boundaries are example rules for this exercise: A = 90-100, B = 75-89, C = 60-74, D = 40-59, and F = 0-39. They should be changed if a real institution uses a different scale.

## 7. Test execution record
Command executed:
```bash
python -m unittest discover -s tests -v
```
Result in the development environment: **34 tests passed, 0 failures, 0 errors.**

## 8. Conclusion
The test suite checks normal operations, validation rules, edge cases, and error conditions across the model, repository, and manager. Integration tests check that the separate parts work together as one workflow. The project uses only Python's standard library and is self-contained.

## Test inventory
The suite contains 34 test methods: 11 model tests, 10 repository tests, 10 manager tests, and 3 integration tests. The grade-boundary method contains multiple subtests to check values at the edge of each band.
