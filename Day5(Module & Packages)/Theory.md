# Modules and packages help you organize and reuse code efficiently. They’re essential for building scalable Python applications.

## 1. What is a Module?

A module is a single Python file (.py) containing functions, classes, or variables you can reuse.

Example: math module
python
import math

print(math.sqrt(25))  # Output: 5.0


Create your own module:
python
## file: greetings.py
def say_hello(name):
    print(f"Hello, {name}!")


Use it:
python
import greetings

greetings.say_hello("Alice")

## 2. What is a Package?

A package is a directory containing multiple modules and a special __init__.py file.

Structure:

my_package/
│
├── __init__.py
├── module1.py
└── module2.py


Usage:
python
from my_package import module1
module1.function_name()

## 3. Import Techniques

- import module
- from module import function
- from module import *
- import module as alias

Example:
python
from math import pi
print(pi)


## 4. Built-in Modules

Python comes with many built-in modules:
- math
- random
- datetime
- os
- sys

Example: random
python
import random
print(random.randint(1, 100))


## 5. Third-Party Packages

Install packages using pip:
bash
pip install numpy


Example:
python
import numpy as np
arr = np.array([1, 2, 3])
print(arr)