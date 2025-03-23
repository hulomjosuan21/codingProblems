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
Given a list of numbers, implement a function `find_min_max(arr)` that returns a tuple containing the minimum and maximum values in the list. The function iterates through the list, updating the minimum and maximum values accordingly.  

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
## Check if a Number is a Palindrome  
Implement a function `is_number_palindrome(n)` that checks whether a given number `n` is a palindrome. A palindrome is a number that reads the same forward and backward.  

```python
def is_number_palindrome(n):
    str_n = str(n)

    reversed_str = ''
    for i in range(len(str_n) - 1, -1, -1):
        reversed_str += str_n[i]

    return True if str_n == reversed_str else False

print(is_number_palindrome(102))  # Output: False
```
## Find the Nth Fibonacci Number  
Implement a function `find_nth_fibonacci_number(n)` that returns the `n`th Fibonacci number. The Fibonacci sequence starts with `0` and `1`, and each subsequent number is the sum of the previous two.  

```python
def find_nth_fibonacci_number(n):
    if n in (0, 1):
        return n

    prev = 0
    curr = 1

    for _ in range(2, n + 1):
        _next = prev + curr
        prev = curr
        curr = _next

    return curr

print(find_nth_fibonacci_number(6))  # Output: 8
```
## Find the Missing Number  
Implement a function `find_missing_number(arr)` that finds the missing number in a sequence of `n` consecutive integers starting from `1`. The function calculates the expected sum of numbers from `1` to `n` using the formula `n * (n + 1) / 2` and compares it to the actual sum of the given list to determine the missing number.  

```python
def find_missing_number(arr):
    n = len(arr) + 1
    expected_sum = n * (n + 1) // 2

    actual_sum = sum(arr)

    return expected_sum - actual_sum

print(find_missing_number([1,2,3,4,5,7,8]))  # Output: 6
```
## Bubble Sort Algorithm  
Implement a function `bubble_sort(arr)` that sorts a list of numbers in ascending order using the Bubble Sort algorithm. The algorithm repeatedly swaps adjacent elements if they are in the wrong order until the entire list is sorted.  

```python
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

print(bubble_sort([1,3,2,5,4]))  # Output: [1, 2, 3, 4, 5]
```
## Merge Two Sorted Arrays  
Implement a function `mergeTwoSortedArray(arr1, arr2)` that merges two sorted arrays into a single sorted array. The function iterates through both arrays, comparing elements and appending the smaller one to the result. Any remaining elements are added at the end.  

```python
def merge_two_sorted_array(arr1, arr2):
    i, j = 0, 0

    merged_arr = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
        else:
            merged_arr.append(arr2[j])
            j += 1

    while i < len(arr1):
        merged_arr.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged_arr.append(arr2[j])
        j += 1

    return merged_arr

print(mergeTwoSortedArray([1,3,5],[2,4,6]))  # Output: [1, 2, 3, 4, 5, 6]
```
## Insertion Sort Algorithm  
Implement a function `insertion_sort(arr)` that sorts a list of numbers in ascending order using the Insertion Sort algorithm. The algorithm builds a sorted sequence one element at a time by shifting larger elements to the right and inserting the current element into its correct position.  

```python
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = temp

    return arr

print(insertion_sort([1,3,2,5,4]))  # Output: [1, 2, 3, 4, 5]
```
## Get All Consonants  
Implement a function `get_consonants()` that prints all consonants from the English alphabet. The function excludes vowels (`a, e, i, o, u`) and prints the remaining letters in lowercase.  

```python
def get_consonants():
    import string

    vowels = "aeiou"

    consonants = [letter for letter in string.ascii_lowercase if letter not in vowels]

    print("".join(consonants))

get_consonants()  # Output: "bcdfghjklmnpqrstvwxyz"
```
## Count Character Frequency in a String  
Implement a function `count_frequency_char_in_str(string)` that counts the frequency of each character in a given string. The function iterates through the string and keeps track of occurrences using a dictionary.  

```python
def count_frequency_char_in_str(string):
    counts = {}

    for c in string:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1

    return counts

print(count_frequency_char_in_str("jjjoosuan"))  
# Output: {'j': 3, 'o': 2, 's': 1, 'u': 1, 'a': 1, 'n': 1}
```
## Find First Non-Repeating Character  
Implement a function `find_first_non_repeating_char(string)` that finds the first character in a given string that does not repeat. The function uses a dictionary to count occurrences and then identifies the first character with a count of `1`.  

```python
def find_first_non_repeating_char(string):
    char_count = {}

    for c in string:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1

    s = ''

    for k, v in char_count.items():
        if v == 1:
            s = k
            break

    return s

print(find_first_non_repeating_char("jjqmsjssaqqq"))  # Output: "m"
```
## Find Median of Two Sorted Arrays  
Implement a function `get_median_of_two_sorted_array(arr1, arr2)` that finds the median of two sorted arrays. The function merges both arrays into a single sorted array and returns the median value.  

```python
def get_median_of_two_sorted_array(arr1, arr2):
    merged_arr = sorted(arr1 + arr2)
    n = len(merged_arr)

    if n % 2 == 0:
        mid1 = n // 2 - 1
        mid2 = n // 2
        return (merged_arr[mid1] + merged_arr[mid2]) / 2
    else:
        return merged_arr[n // 2]

print(get_median_of_two_sorted_array([1, 3, 5], [2, 4, 6]))  # Output: 3.5
```
## Two Sum Problem  
Implement a function `two_sum_problem(arr, target)` that finds the indices of two numbers in an array that add up to a given target. The function iterates through the array and returns the first pair of indices whose sum equals the target.  

```python
def two_sum_problem(arr, target):
    n = len(arr)
    x, y = -1, -1
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                x, y = i, j
                break
        if x != -1:
            break

    return [x, y]

print(two_sum_problem([2, 7, 11, 15], 9))  # Output: [0, 1]
```
## Check If a String is a Palindrome  
Implement a function `check_if_palindrome(string)` that checks whether a given string is a palindrome. A palindrome is a word, phrase, or sequence that reads the same forward and backward.  

```python
def check_if_palindrome(string):
    i, j = 0, len(string) - 1
    while i < j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True

print(check_if_palindrome("level"))  # Output: True
print(check_if_palindrome("hello"))  # Output: False
```
## Digital Decipher
```python
def digital_decipher(s, key):
    ascii_val = [ord(i) for i in s]

    result = ''
    for n in ascii_val:
        result += chr(n-key)

    return result
```
