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
def findMinMax(arr) -> tuple:
    _min, _max = arr[0], arr[0]

    for e in arr:
        if e < _min:
            _min = e
        if e > _max:
            _max = e

    return _min, _max

print(findMinMax([1,2,3]))
```
