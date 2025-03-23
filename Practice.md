## Reverse Index Iteration
```python
n = 5

i, j = 0, n-1

while i < n:
    print(f"{i} : {j}")

    i += 1
    j -= 1

# Output 
# 0 : 4
# 1 : 3
# 2 : 2
# 3 : 1
# 4 : 0
```
## Range Parameters in Python
``` python
for i in range(start, stop, step):
```
#### 1. Comparison Operators (Relational Operators)  
These compare two values and return `True` or `False`.

| Operator | Description              | Example (`a = 5, b = 10`) |
|----------|--------------------------|---------------------------|
| `==`     | Equal to                 | `a == b  → False`         |
| `!=`     | Not equal to             | `a != b  → True`          |
| `>`      | Greater than             | `a > b   → False`         |
| `<`      | Less than                | `a < b   → True`          |
| `>=`     | Greater than or equal to | `a >= b  → False`         |
| `<=`     | Less than or equal to    | `a <= b  → True`          |

#### 2. Logical Operators  
These are used to combine conditional statements.

| Operator | Description                          | Example (`x = True, y = False`) |
|----------|--------------------------------------|---------------------------------|
| `and`    | Returns `True` if both are `True`   | `x and y  → False`             |
| `or`     | Returns `True` if at least one is `True` | `x or y → True`           |
| `not`    | Reverses the boolean value         | `not x  → False`              |

#### 3. Membership Operators  
These check if a value exists in a sequence (like a list, tuple, or string).

| Operator | Description                      | Example (`lst = [1, 2, 3]`) |
|----------|----------------------------------|-----------------------------|
| `in`     | Returns `True` if value is found | `2 in lst → True` |
| `not in` | Returns `True` if value is NOT found | `5 not in lst → True` |

#### 4. Identity Operators  
These compare memory locations of objects.

| Operator | Description                          | Example (`a = 5, b = 5, c = [1,2]`) |
|----------|--------------------------------------|-------------------------------------|
| `is`     | Returns `True` if both refer to the same object | `a is b → True` |
| `is not` | Returns `True` if they refer to different objects | `a is not c → True` |
