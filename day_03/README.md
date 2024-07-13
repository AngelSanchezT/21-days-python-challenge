# ✅ Exercise 03 - Determine if a Year is a Leap Year

In this Python challenge, you need to create the logic for the function `is_leap_year`, which determines if a year is a leap year or not. A year is a leap year if it meets the following conditions:

- It is divisible by 4 but not by 100.
- If it is divisible by 100, it must also be divisible by 400.

The function `is_leap_year` receives a single parameter: the year to evaluate. It should return `True` if the year is a leap year or `False` otherwise.

Note that the function must be able to handle non-integer or negative values.

Example 1:

```python
Input: 2000;
Output: true;
```

Example 2:

```python
Input: -2024;
Output: false;
```

Example 3:

```python
Input: 1984.25;
Output: false;
```

# ✅ Exercise 04 - Draw a Triangle Using Loops

In this challenge, you need to draw an equilateral triangle using loops.

You will receive two parameters: `size` and `character`, which define the number of rows and the character used to build the triangle, respectively. Additionally, the triangle must be center-aligned, meaning it should have the same number of characters on both sides.

> Remember that to make a line break you need to use "\n", do not forget to remove it from the last part, you must return all this in a variable.

You will have inputs and outputs like the following 👇

Example 1:

```python
Input: printTriangle(3, "*")
Output:
  *
 ***
*****
```

Ejemplo 2:

```python
Input: printTriangle(6, "$")
Output:
     $
    $$$
   $$$$$
  $$$$$$$
 $$$$$$$$$
$$$$$$$$$$$
```
