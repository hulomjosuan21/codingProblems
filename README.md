## Prime Number Checker 
A prime number is a natural number greater than 1 that has only two factors: 1 and itself. The goal is to implement a function `is_prime_number(n)` that checks whether a given number `n` is prime. The function should return `True` if the number is prime and `False` otherwise.  

```python
import math

def is_prime_number(n):
    is_prime = True
    if n <= 1:
        is_prime = False
    elif n in (2, 3):
        pass
    elif n % 2 == 0:
        is_prime = False
    else:
        for i in range(3, math.isqrt(n) + 1, 2):
            if n % i == 0:
                is_prime = False
                break

    return is_prime

result = "Prime" if is_prime_number(8) else "Not Prime"
print(result)  # Output: Not Prime
```
## Find Minimum and Maximum  
Given a list of numbers, implement a function `findMinMax(arr)` that returns a tuple containing the minimum and maximum values in the list. The function iterates through the list, updating the minimum and maximum values accordingly.  

```python
def find_min_max(arr):
    _min, _max = arr[0], arr[0]

    for e in arr:
        if e < _min:
            _min = e
        if e > _max:
            _max = e

    return _min, _max

print(findMinMax([1,2,3])) # Output: "(1,3)"
```
Reverse a String  
Implement a function `reverse_string(text)` that takes a string as input and returns the reversed version of it. The function iterates through the string in reverse order and constructs a new reversed string.  

```python
def reverse_string(text):
    temp = ''
    # temp = text[::-1]

    for i in range(len(text) - 1, -1, -1):
        temp += text[i]

    return temp

print(reverse_string("Josuan"))  # Output: "nausoJ"
```
## Compute Factorial of a Number  
Implement a function `compute_factorial_of_number(n)` that calculates the factorial of a given non-negative integer `n`. The factorial of a number `n` is the product of all positive integers from `1` to `n`.  

```python
def compute_factorial_of_number(n):
    if n in (0, 1):
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i

    return result

print(compute_factorial_of_number(5))  # Output: 120
```
## Find Greatest Common Divisor (GCD)  
Implement a function `find_GCD(a, b)` that calculates the greatest common divisor (GCD) of two integers `a` and `b` using the Euclidean algorithm. The GCD is the largest positive integer that divides both numbers without leaving a remainder.  

```python
def find_GCD(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

print(find_GCD(48, 18))  # Output: 6
```
