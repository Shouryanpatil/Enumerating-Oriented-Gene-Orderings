# Enumerating Oriented Gene Orderings

## Problem Statement
A signed permutation of length `n` is an arrangement of the integers `{1, 2, ..., n}` where each number is assigned either a positive or negative sign. For example, `(-1, 2)` is a signed permutation of length 2.

The task is:
1. Given a positive integer `n` (where `1 <= n <= 6`), compute all signed permutations of length `n`.
2. Print the total number of signed permutations.
3. Output the list of all signed permutations (each on a new line).

---

## Formula
Total number of signed permutations of `n`:
```
n! * 2^n
```
Where `n!` is the factorial of `n` and `2^n` accounts for the two sign possibilities per element.

---

## Example
**Input:**
```
2
```

**Output:**
```
8
-1 -2
-1 2
1 -2
1 2
-2 -1
-2 1
2 -1
2 1
```

---

## Usage
Run the script with a value of `n` (between 1 and 6):

```python
python signed_permutations.py
```

Edit the last line of the file to set the desired value of `n`:
```python
n = 2  # Change this to any value from 1 to 6
```

---

## File
**`signed_permutations.py`** - Contains the implementation of the solution using `itertools.permutations` and `itertools.product`.

---

## Dependencies
- Python 3.x
- No external libraries needed

---

## License
This project is open-source and free to use under the MIT License.

