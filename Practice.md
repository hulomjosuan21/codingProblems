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
## Python Conditional Operators
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
## Built-in Function
# Python Built-in Functions

## 1. `sum()`
**Description:** Returns the sum of all items in an iterable.  
**Example:** `sum([1, 2, 3])` → `6`

## 2. `next()`
**Description:** Retrieves the next item from an iterator.  
**Example:** `next(iter([10, 20, 30]))` → `10`

## 3. `ord()`
**Description:** Returns the Unicode code of a character.  
**Example:** `ord('A')` → `65`

## 4. `chr()`
**Description:** Returns the character for a Unicode code.  
**Example:** `chr(65)` → `'A'`

---

## Full List of Python Built-in Functions:

| Function       | Description | Example |
|---------------|------------|---------|
| `abs(x)` | Returns the absolute value of `x`. | `abs(-5) → 5` |
| `all(iterable)` | Returns `True` if all elements in `iterable` are `True`. | `all([True, 1, "abc"]) → True` |
| `any(iterable)` | Returns `True` if any element in `iterable` is `True`. | `any([False, 0, "abc"]) → True` |
| `ascii(obj)` | Returns a string with non-ASCII characters escaped. | `ascii("ñ") → "'\\xf1'"` |
| `bin(x)` | Converts an integer to a binary string. | `bin(5) → '0b101'` |
| `bool(x)` | Converts `x` to a boolean. | `bool([]) → False` |
| `breakpoint()` | Starts a debugger at that point. | `breakpoint()` |
| `bytearray(x)` | Returns a mutable bytes array. | `bytearray(4) → bytearray(b'\x00\x00\x00\x00')` |
| `bytes(x)` | Returns an immutable bytes object. | `bytes(4) → b'\x00\x00\x00\x00'` |
| `callable(obj)` | Checks if `obj` is callable. | `callable(len) → True` |
| `chr(x)` | Returns character for Unicode `x`. | `chr(97) → 'a'` |
| `classmethod(func)` | Converts a function into a class method. | `@classmethod` |
| `compile(src, filename, mode)` | Compiles source into a code object. | `compile('x=5', '', 'exec')` |
| `complex(real, imag)` | Creates a complex number. | `complex(2, 3) → (2+3j)` |
| `delattr(obj, name)` | Deletes attribute `name` from `obj`. | `delattr(obj, 'attr')` |
| `dict()` | Creates a dictionary. | `dict(a=1, b=2) → {'a': 1, 'b': 2}` |
| `dir(obj)` | Returns attributes of an object. | `dir([])` |
| `divmod(a, b)` | Returns `(a // b, a % b)`. | `divmod(10, 3) → (3, 1)` |
| `enumerate(iterable)` | Returns an enumerated iterable. | `list(enumerate(['a', 'b'])) → [(0, 'a'), (1, 'b')]` |
| `eval(expr)` | Evaluates an expression string. | `eval('2 + 3') → 5` |
| `exec(code)` | Executes a block of Python code. | `exec('x = 5')` |
| `filter(func, iterable)` | Filters elements using `func`. | `list(filter(lambda x: x > 2, [1, 2, 3])) → [3]` |
| `float(x)` | Converts `x` to a float. | `float("5.3") → 5.3` |
| `format(value, format_spec)` | Formats a value. | `format(255, 'x') → 'ff'` |
| `frozenset(iterable)` | Creates an immutable set. | `frozenset([1, 2, 3])` |
| `getattr(obj, name)` | Gets attribute `name` of `obj`. | `getattr(obj, 'attr')` |
| `globals()` | Returns global variables dictionary. | `globals()` |
| `hasattr(obj, name)` | Checks if `obj` has attribute `name`. | `hasattr(obj, 'attr')` |
| `hash(obj)` | Returns hash of an object. | `hash('hello')` |
| `help(obj)` | Shows help for `obj`. | `help(print)` |
| `hex(x)` | Converts `x` to a hexadecimal string. | `hex(255) → '0xff'` |
| `id(obj)` | Returns object's memory address. | `id([])` |
| `input(prompt)` | Reads input from the user. | `input("Enter: ")` |
| `int(x)` | Converts `x` to an integer. | `int("42") → 42` |
| `isinstance(obj, type)` | Checks if `obj` is an instance of `type`. | `isinstance(5, int) → True` |
| `issubclass(sub, super)` | Checks subclass relationship. | `issubclass(bool, int) → True` |
| `iter(iterable)` | Returns an iterator. | `iter([1, 2, 3])` |
| `len(obj)` | Returns length of `obj`. | `len("abc") → 3` |
| `list(iterable)` | Converts `iterable` to a list. | `list("abc") → ['a', 'b', 'c']` |
| `locals()` | Returns local variables dictionary. | `locals()` |
| `map(func, iterable)` | Maps `func` over `iterable`. | `list(map(str.upper, "abc")) → ['A', 'B', 'C']` |
| `max(iterable)` | Returns max value. | `max([1, 2, 3]) → 3` |
| `min(iterable)` | Returns min value. | `min([1, 2, 3]) → 1` |
| `object()` | Creates a new object. | `object()` |
| `oct(x)` | Converts `x` to octal. | `oct(8) → '0o10'` |
| `open(filename, mode)` | Opens a file. | `open('file.txt', 'r')` |
| `pow(x, y, mod)` | Computes `(x ** y) % mod`. | `pow(2, 3, 5) → 3` |
| `print(*args)` | Prints values. | `print("Hello")` |
| `range(start, stop, step)` | Generates a range of numbers. | `list(range(1, 5)) → [1, 2, 3, 4]` |
| `repr(obj)` | Returns string representation. | `repr(5) → '5'` |
| `reversed(seq)` | Returns reversed iterator. | `list(reversed([1, 2, 3])) → [3, 2, 1]` |
| `round(x, n)` | Rounds `x` to `n` decimal places. | `round(3.1415, 2) → 3.14` |
| `set(iterable)` | Creates a set. | `set([1, 2, 2, 3]) → {1, 2, 3}` |
| `sorted(iterable)` | Returns sorted list. | `sorted([3, 1, 2]) → [1, 2, 3]` |
| `str(obj)` | Converts `obj` to string. | `str(42) → '42'` |
| `sum(iterable)` | Returns sum of elements. | `sum([1, 2, 3]) → 6` |
| `tuple(iterable)` | Converts `iterable` to tuple. | `tuple([1, 2, 3]) → (1, 2, 3)` |
| `zip(*iterables)` | Zips iterables together. | `list(zip([1, 2], ['a', 'b'])) → [(1, 'a'), (2, 'b')]` |
