# Python Learning Journal

This repository contains my daily learning progress as I go through Python fundamentals and descriptive statistics — part of my M.Sc. job-ready skill-building plan.

---

### ✅ Day 1: Python Setup & Syntax
- Practiced: `print()`, `input()`, `type()`, type conversions (`int`, `float`, `complex`, `str`)
- Learned how to:
  - Use `.split()` with `input()`
  - Convert between data types
  - Use comments for documentation

---

### ✅ Day 2: Data Structures – Lists, Tuples, Sets, Dictionaries
- Practiced:
  - List operations (`append`, `pop`, `sort`, slicing)
  - Tuple immutability
  - Set properties (no duplicates, basic set operations)
  - Dictionary creation, key-value pairs, `get()`, `update()`, `keys()`, `values()`
- Learned differences between these structures and where to use them

---

### ✅ Day 3: Conditional Statements
- Practiced:
  - `if`, `elif`, `else` statements
  - Nested conditions
  - Logical operators: `and`, `or`, `not`
- Built small programs using conditional logic (e.g., grading system, eligibility check)

---

### ✅ Day 4: Loops – `for` and `while`
- Practiced:
  - `for` loop with `range()`
  - Iterating over strings and lists
  - `while` loop with exit conditions
  - Control statements: `break`, `continue`, `pass`
- Wrote mini-examples like printing patterns, list search, sum calculator

---

### ✅ Day 5: Functions
- Practiced:
  - Creating and calling functions using `def`
  - Using parameters and `return` values

- Wrote modular functions for repeated tasks

---

### ✅ Day 6: Random ,Math &  Statistics Modules (Additional)
- Practiced:
  - `math` module: `sqrt`, `floor`, `ceil`, `pow`, `factorial`, `pi`
  - `statistics` module: `mean`, `median`, `mode`, `variance`, `stdev`, `pvariance`, `pstdev`
- Used both modules in practice scripts to perform calculations and summaries

---

### ✅ Day 7: Mini Project – Descriptive Statistics Tool

This project analyzes a list of numbers entered by the user and outputs key descriptive statistics using only built-in modules (`statistics`, `math`).

#### 🧠 Features:
- Count, Mean, Median, Mode(s)
- Min, Max, Range
- Population & Sample Variance and Standard Deviation
- Quartiles (Q1, Q2, Q3), IQR
- Outlier detection using 1.5×IQR rule

#### 📦 Python Concepts Used:
- `input()`, lists, loops, conditionals, and custom functions
- Built-in modules: `math`, `statistics`

#### 📂 File:
`Week1_Python/mini_proj1.py` ---- in python
`Week1_Python/mini_proj1.ipynb` ---- in jupyter notebook

#### SAMPLE OUTPUT #####

Enter your data with space between each data points= 2 4 2 79 173 182 2 3 4 44 5 3 22
Entered data is=  [2.0, 4.0, 2.0, 79.0, 173.0, 182.0, 2.0, 3.0, 4.0, 44.0, 5.0, 3.0, 22.0]
-----For The Given Data The Following Statistics Are Calculated And Are Listed Below----

ABOUT THE DATA ,  [2.0, 4.0, 2.0, 79.0, 173.0, 182.0, 2.0, 3.0, 4.0, 44.0, 5.0, 3.0, 22.0]
NO OF ELEMENTS IN DATA SET IS : 13
DATA HAS ODD NO OF ELEMENTS

SECTION-1 "__MEASURE OF CENTRAL TENDANCIES__"

MEAN:                                   40.38461538461539
MEDIAN:                                 4.0
UNIQUE MODE:                            [2.0]

SECTION-2 "__MEASURE OF DISPERSION__"

POPULATION VARIANCE:                    3892.24
SAMPLE VARIANCE:                        4216.59
POPULATION STANDARD DEVIATION:          62.39
SAMPLE STANDARD DEVIATION:              64.94

SECTION-3 "__MEASURE OF RANGE __"

MAXIMUM VALUE OF THE DATA SET:          182.0
MINIMUM VALUE OF THE DATA SET:          2.0
RANGE OF THE DATA SET:                  180.0

SECTION-4 "__MEASURE OF POSITION__"

QUARTILE 1:                             2.5
QUARTILE 2:                             4.0
QUARTILE 3:                             61.5
INTER QUARTILE RANGE:                   59.0
OUTLIARS:                             [173.0, 182.0]

Do you want to do it for another data set ?(y/n)


#### 🧪 Sample Output
