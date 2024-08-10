<p align="center">
  <img src="https://res.cloudinary.com/dg4bxglze/image/upload/w_150,h_150,c_fill,g_face,r_max/v1723224449/oi4o4qghqwosobxpo0ea.png" alt="NumLex Logo">
</p>

# NumLex

NumLex is a Python package that provides a collection of mathematical and string manipulation functions. It includes modules for geometry, arithmetic, probability, statistics, string operations, and number operations, making it a versatile tool for various computational tasks.

## Installation

You can install NumLex via pip:

```bash
pip install numlex
```

## Modules and Functions

### 1. Geometry (`m.geo.py`)

- **Area Of Triangle**: Calculate the area of a triangle.
- **Area Of Circle**: Calculate the area of a circle.
- **Area Of Rectangle**: Calculate the area of a rectangle.
- **Area Of Square**: Calculate the area of a square.

### 2. Arithmetic (`m.arith.py`)

- **Modular Arithmetic**: Perform modular addition, subtraction, and multiplication.
- **Roots**: Calculate square, cube, and nth roots.
- **Factorials**: Compute the factorial of a number.

### 3. Probability (`m.prob.py`)

- **Permutations**: Calculate the number of permutations.
- **Combinations**: Calculate the number of combinations.

### 4. Statistics (`m.stats.py`)

- **Ungroup Mean**: Calculate the mean for ungrouped data.
- **Group Mean**: Calculate the mean for grouped data.
- **Median**: Find the median of a dataset.
- **Ungroup Mode**: Determine the mode for ungrouped data.
- **Raw Mode**: Determine the raw mode of data.
- **Variance**: Calculate the variance of data.
- **Standard Deviation**: Calculate the standard deviation of data.

### 5. String Operations (`str_ops.py`)

- **Vowel**: Check if a character is a vowel.
- **Consonant**: Check if a character is a consonant.
- **Search Char From String**: Search for a character in a string.
- **Palindrome Checker**: Check if a string is a palindrome.
- **Character Counting**: Count the occurrences of each character in a string.

### 6. Number Operations (`num_ops.py`)

- **Max From Given Numbers**: Find the maximum value from a list of numbers.
- **Min From Given Numbers**: Find the minimum value from a list of numbers.
- **Total Of Given Numbers**: Calculate the total of a list of numbers (options for even and odd totals).
- **Square Of Numbers**: Compute the square of numbers.
- **Positive / Negative / Zero**: Determine if a number is positive, negative, or zero.
- **Odd / Even**: Check if a number is odd or even.
- **Leap Year / !Leap Year**: Check if a year is a leap year.
- **Total Of Digits Of Number**: Calculate the sum of the digits of a number.
- **Reverse Of Number**: Reverse the digits of a number.
- **Palindrome Checker**: Check if a number is a palindrome.
- **Length Of Number**: Determine the length of a number.

## Useful Links

- You can checkout the package details also on the Python package Index [here](https://pypi.org/project/NumLex/)
- You can checkout the package wiki at github wikis [here](https://github.com/Jenil-Desai/NumLex/wiki)
- You can checkout the package version releases on the Notion Page [here](https://jenil-desai.notion.site/Version-Releases-NumLex-aae7fe2fee39415d93e19931aa7c7118?pvs=4)

## Usage

Here is an example of how to use the NumLex package:

```python
from NumLex.m.geo import area_triangle
from NumLex.m.arith import fact
from NumLex.num_ops import max_num

# Calculate the area of a triangle
area = area_triangle(base=10, height=5)
print("Area of Triangle:", area)

# Calculate the factorial of a number
fact = fact(5)
print("Factorial:", fact)

# Find the maximum number in a list
max_num = max_Num([1, 2, 3, 4, 5])
print("Maximum Number:", max_num)
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
