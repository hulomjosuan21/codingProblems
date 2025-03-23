## Get key by value of python dictionary
```python
key = next(k for k, v in my_dict.items() if v == 10)
```
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

## Full List of Python Built-in Functions:
| Function       | Description | Example |
|---------------|------------|---------|
| `sum(iterable)` | Returns the sum of all items in an iterable. | `sum([1, 2, 3]) → 6` |
| `next(iterator)` | Retrieves the next item from an iterator. | `next(iter([10, 20, 30])) → 10` |
| `ord(char)` | Returns the Unicode code of a character. | `ord('A') → 65` |
| `chr(code)` | Returns the character for a Unicode code. | `chr(65) → 'A'` |
| `abs(x)` | Returns the absolute value of `x`. | `abs(-5) → 5` |
| `map(func, iterable, ...)` | Applies a function to all items in an iterable and returns a map object. | `map(str.upper, ['a', 'b', 'c']) → ['A', 'B', 'C']` |
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

## Python Math Built-in Functions

| Function | Description | Example |
|----------|------------|---------|
| `abs(x)` | Returns the absolute value of `x`. | `abs(-5) → 5` |
| `divmod(a, b)` | Returns a tuple `(a // b, a % b)`. | `divmod(10, 3) → (3, 1)` |
| `max(iterable, *args)` | Returns the maximum value. | `max([1, 5, 3]) → 5` |
| `min(iterable, *args)` | Returns the minimum value. | `min([1, 5, 3]) → 1` |
| `pow(x, y, mod)` | Returns `(x ** y) % mod` (if `mod` is given). | `pow(2, 3) → 8` |
| `round(x, n)` | Rounds `x` to `n` decimal places. | `round(3.1415, 2) → 3.14` |
| `sum(iterable, start)` | Returns the sum of all items in an iterable. | `sum([1, 2, 3]) → 6` |
| `bin(x)` | Converts an integer to a binary string. | `bin(5) → '0b101'` |
| `hex(x)` | Converts an integer to a hexadecimal string. | `hex(255) → '0xff'` |
| `oct(x)` | Converts an integer to an octal string. | `oct(8) → '0o10'` |
| `math.prod(iterable)` | Returns the product of all elements in an iterable. | `math.prod([2, 3, 4]) → 24` |
| `math.factorial(x)` | Returns the factorial of `x`. | `math.factorial(5) → 120` |
| `math.gcd(a, b)` | Returns the greatest common divisor of `a` and `b`. | `math.gcd(8, 12) → 4` |
| `math.lcm(a, b)` | Returns the least common multiple of `a` and `b`. | `math.lcm(8, 12) → 24` |
| `math.isqrt(x)` | Returns the integer square root of `x`. | `math.isqrt(10) → 3` |
| `math.sqrt(x)` | Returns the square root of `x`. | `math.sqrt(16) → 4.0` |
| `math.exp(x)` | Returns `e ** x`. | `math.exp(2) → 7.389` |
| `math.log(x, base)` | Returns the logarithm of `x` to the given base. | `math.log(8, 2) → 3.0` |
| `math.log10(x)` | Returns the base-10 logarithm of `x`. | `math.log10(100) → 2.0` |
| `math.log2(x)` | Returns the base-2 logarithm of `x`. | `math.log2(8) → 3.0` |
| `math.sin(x)` | Returns the sine of `x` (radians). | `math.sin(math.pi / 2) → 1.0` |
| `math.cos(x)` | Returns the cosine of `x` (radians). | `math.cos(0) → 1.0` |
| `math.tan(x)` | Returns the tangent of `x` (radians). | `math.tan(math.pi / 4) → 1.0` |
| `math.degrees(x)` | Converts radians to degrees. | `math.degrees(math.pi) → 180.0` |
| `math.radians(x)` | Converts degrees to radians. | `math.radians(180) → 3.1416` |
| `math.ceil(x)` | Returns the smallest integer greater than or equal to `x`. | `math.ceil(3.2) → 4` |
| `math.floor(x)` | Returns the largest integer less than or equal to `x`. | `math.floor(3.8) → 3` |
| `math.trunc(x)` | Truncates `x`, removing the decimal part. | `math.trunc(3.9) → 3` |
| `math.copysign(x, y)` | Returns `x` with the sign of `y`. | `math.copysign(3, -1) → -3.0` |
| `math.fabs(x)` | Returns the absolute value of `x`. | `math.fabs(-3.5) → 3.5` |
| `math.fmod(x, y)` | Returns the remainder of `x / y`. | `math.fmod(10, 3) → 1.0` |
| `math.frexp(x)` | Returns `(m, e)` such that `x = m * 2**e`. | `math.frexp(8) → (0.5, 4)` |
| `math.modf(x)` | Returns the fractional and integer parts of `x`. | `math.modf(3.5) → (0.5, 3.0)` |
| `math.hypot(x, y)` | Returns the Euclidean norm, `sqrt(x² + y²)`. | `math.hypot(3, 4) → 5.0` |

## Python `itertools` Functions

| Function | Description | Example |
|----------|------------|---------|
| `itertools.count(start, step)` | Returns an infinite iterator that counts from `start`, incrementing by `step`. | `count(10, 2) → 10, 12, 14, ...` |
| `itertools.cycle(iterable)` | Cycles through an iterable indefinitely. | `cycle([1, 2, 3]) → 1, 2, 3, 1, 2, 3, ...` |
| `itertools.repeat(item, n)` | Repeats an item `n` times (or indefinitely if `n` is not given). | `repeat(5, 3) → 5, 5, 5` |
| `itertools.permutations(iterable, r)` | Returns all possible `r`-length permutations of elements. | `permutations([1, 2, 3], 2) → (1,2), (1,3), (2,1), ...` |
| `itertools.combinations(iterable, r)` | Returns all possible `r`-length combinations (order doesn’t matter). | `combinations([1, 2, 3], 2) → (1,2), (1,3), (2,3)` |
| `itertools.combinations_with_replacement(iterable, r)` | Like `combinations()`, but allows repeated elements. | `combinations_with_replacement([1, 2], 2) → (1,1), (1,2), (2,2)` |
| `itertools.product(*iterables, repeat=n)` | Returns Cartesian product of input iterables. | `product([1, 2], [3, 4]) → (1,3), (1,4), (2,3), (2,4)` |
| `itertools.chain(*iterables)` | Chains multiple iterables together. | `chain([1, 2], [3, 4]) → 1, 2, 3, 4` |
| `itertools.islice(iterable, start, stop, step)` | Slices an iterable like `list[start:stop:step]`. | `islice(range(10), 2, 8, 2) → 2, 4, 6` |
| `itertools.compress(data, selectors)` | Filters `data`, keeping only items where `selectors` is `True`. | `compress('ABC', [1, 0, 1]) → 'A', 'C'` |
| `itertools.dropwhile(predicate, iterable)` | Drops elements while `predicate` is `True`, then returns the rest. | `dropwhile(lambda x: x < 5, [1, 3, 5, 7]) → 5, 7` |
| `itertools.takewhile(predicate, iterable)` | Returns elements while `predicate` is `True`, then stops. | `takewhile(lambda x: x < 5, [1, 3, 5, 7]) → 1, 3` |
| `itertools.tee(iterable, n)` | Creates `n` independent iterators from a single iterable. | `tee([1, 2, 3], 2) → (iterator1, iterator2)` |
| `itertools.groupby(iterable, key)` | Groups elements based on a key function. | `groupby('AAABBBCC', key=lambda x: x) → ('A', 'AAA'), ('B', 'BBB'), ('C', 'CC')` |
| `itertools.starmap(function, iterable)` | Applies a function to arguments unpacked from iterable tuples. | `starmap(pow, [(2,5), (3,2)]) → 32, 9` |
| `itertools.accumulate(iterable, func)` | Returns accumulated results using `func` (default is sum). | `accumulate([1, 2, 3, 4]) → 1, 3, 6, 10` |

## Python `collections` Module

| Function / Class | Description | Example |
|------------------|------------|---------|
| `collections.Counter(iterable)` | A dictionary subclass for counting elements. | `Counter("banana") → {'a': 3, 'n': 2, 'b': 1}` |
| `collections.defaultdict(default_factory)` | A dictionary that provides a default value for missing keys. | `defaultdict(int)['x'] → 0` |
| `collections.OrderedDict()` | A dictionary that maintains insertion order (since Python 3.7, `dict` does this too). | `OrderedDict([('a', 1), ('b', 2)])` |
| `collections.deque(iterable, maxlen)` | A double-ended queue supporting fast appends and pops. | `deque([1, 2, 3]).appendleft(0) → deque([0, 1, 2, 3])` |
| `collections.namedtuple(typename, field_names)` | Creates a tuple subclass with named fields. | `Point = namedtuple('Point', 'x y'); Point(1, 2) → Point(x=1, y=2)` |
| `collections.ChainMap(*dicts)` | Groups multiple dictionaries into a single view. | `ChainMap({'a': 1}, {'b': 2})['a'] → 1` |
| `collections.UserDict()` | A wrapper around a standard dictionary that can be subclassed. | `class MyDict(UserDict): pass` |
| `collections.UserList()` | A wrapper around a standard list that can be subclassed. | `class MyList(UserList): pass` |
| `collections.UserString()` | A wrapper around a standard string that can be subclassed. | `class MyStr(UserString): pass` |

# Python `asyncio` Module

| Function / Class | Description | Example |
|------------------|------------|---------|
| `asyncio.run(coro)` | Runs an async function (coroutine) and manages the event loop. | `asyncio.run(main())` |
| `asyncio.create_task(coro)` | Creates and schedules an asynchronous task. | `task = asyncio.create_task(my_coro())` |
| `asyncio.sleep(seconds)` | Asynchronously sleeps for the given time. | `await asyncio.sleep(2)` |
| `asyncio.gather(*coros)` | Runs multiple async functions concurrently and gathers results. | `await asyncio.gather(task1(), task2())` |
| `asyncio.wait(tasks)` | Runs multiple tasks concurrently and waits for completion. | `await asyncio.wait([task1(), task2()])` |
| `asyncio.shield(coro)` | Protects a coroutine from being cancelled. | `await asyncio.shield(task)` |
| `asyncio.TimeoutError` | Raised when an operation exceeds a timeout. | `raise asyncio.TimeoutError()` |
| `asyncio.Queue(maxsize=0)` | A FIFO async queue for inter-task communication. | `queue = asyncio.Queue(); await queue.put(10)` |
| `asyncio.Lock()` | An asynchronous lock for synchronizing coroutines. | `lock = asyncio.Lock(); async with lock: ...` |
| `asyncio.Event()` | An async event to notify coroutines. | `event = asyncio.Event(); await event.wait()` |
| `asyncio.Condition()` | An async condition variable for coroutine synchronization. | `cond = asyncio.Condition(); async with cond: ...` |
| `asyncio.Semaphore(value=1)` | Limits concurrency by allowing only `value` tasks at a time. | `sem = asyncio.Semaphore(2); async with sem: ...` |
| `asyncio.run_coroutine_threadsafe(coro, loop)` | Runs a coroutine from a different thread. | `asyncio.run_coroutine_threadsafe(coro, loop)` |
| `asyncio.Loop.create_task(coro)` | Schedules a coroutine as a task in an existing loop. | `loop.create_task(my_coro())` |
| `asyncio.Loop.run_forever()` | Runs the event loop indefinitely. | `loop.run_forever()` |
| `asyncio.Loop.stop()` | Stops the event loop. | `loop.stop()` |

## Python `functools` Module

| Function | Description | Example |
|----------|------------|---------|
| `functools.reduce(func, iterable, init)` | Applies a function cumulatively to items in an iterable, reducing it to a single value. | `reduce(lambda x, y: x + y, [1, 2, 3, 4]) → 10` |
| `functools.lru_cache(maxsize=None)` | Caches the results of a function to improve performance. | `@lru_cache(maxsize=128) def fib(n): return n if n < 2 else fib(n-1) + fib(n-2)` |
| `functools.partial(func, *args, **kwargs)` | Returns a new function with fixed arguments. | `double = partial(lambda x, y: x * y, 2); double(5) → 10` |
| `functools.singledispatch(func)` | Creates a generic function that can be specialized for different types. | `@singledispatch def process(val): print("General"); @process.register(int) def _(val): print("Integer")` |
| `functools.wraps(wrapper)` | Preserves the original function’s metadata when wrapping it with another function. | `@wraps(original_func) def wrapper(): pass` |
| `functools.cmp_to_key(func)` | Converts an old-style comparison function into a key function for sorting. | `sorted([5, 2, 4], key=cmp_to_key(lambda x, y: x - y))` |
| `functools.total_ordering(cls)` | Generates missing comparison methods for a class. | `@total_ordering class MyClass: def __lt__(self, other): ...` |
