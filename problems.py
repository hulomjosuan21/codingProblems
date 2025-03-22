import math

from jinja2.utils import missing


class CodingProblems1:
    statement = "Coding problems that I solve during my practice for coding competition"

    def __str__(self):
        return self.statement

    def __repr__(self):
        return self.statement

    @staticmethod
    def isPrimeNumber(n):
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

    @staticmethod
    def findMinMax(arr) -> tuple:
        _min, _max = arr[0], arr[0]

        # for i in range(len(arr)):
        #     if arr[i] < _min:
        #         _min = arr[i]
        #     if arr[i] > _max:
        #         _max = arr[i]

        for e in arr:
            if e < _min:
                _min = e
            if e > _max:
                _max = e

        return _min, _max

    @staticmethod
    def reverseAString(text) -> str:
        temp = ''

        # temp = text[::-1]

        for i in range(len(text)-1,-1,-1):
            temp += text[i]

        return temp

    @staticmethod
    def computeFactorialOfANumber(n):
        if n in (0,1):
            return 1

        result = 1
        for i in range(2, n+1):
            result *= i

        return result

    @staticmethod
    def findGCD(a,b):
        if a <= 0 or b <= 0:
            return 0

        while b > 0:
            temp = b
            b = a % b
            a = temp

        return a

    @staticmethod
    def isNumberPalindrome(n) -> str:
        str_n = str(n)

        reversed_str = ''
        for i in range(len(str_n) - 1, -1, -1):
            reversed_str += str_n[i]

        return f"{n} is Palindrome {str_n} : {reversed_str}" if str_n == reversed_str else f"{n} is not Palindrome {str_n} : {reversed_str}"

    @staticmethod
    def findNthFibonacciNumber(n):
        if n in (0,1):
            return n

        prev = 0
        curr = 1

        for _ in range(2, n+1):
            _next = prev + curr
            prev = curr
            curr = _next

        return curr

    @staticmethod
    def findMissingNumber(arr,n):
        expected_sum = n * (n+1) // 2

        actual_sum = 0
        for n in arr:
            actual_sum += n

        # actual_sum = sum(arr)

        return expected_sum - actual_sum

    @staticmethod
    def bubbleSort(arr):
        n = len(arr)

        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

        return arr

    @staticmethod
    def mergeTwoSortedArray(arr1,arr2) -> []:
        i,j = 0,0

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

    @staticmethod
    def insertionSort(arr):
        n = len(arr)
        for i in range(1, n):
            temp = arr[i]
            j = i - 1

            while j >= 0 and arr[j] > temp:
                arr[j+1] = arr[j]
                j -= 1

            arr[j+1] = temp


    @staticmethod
    def findLongestCommonPrefix(arr):
        shortest_str = arr[0]

        for c in arr:
            if len(c) < len(shortest_str):
                shortest_str = c

        for i in range(len(shortest_str)):
            char = shortest_str[i]
            for s in arr:
                if s[i] != char:
                    return  shortest_str[:i]

        return shortest_str

    @staticmethod
    def findFirstNonRepeatingCharacter(string):
        ...

    @staticmethod
    def getConsonants():
        import string

        vowels = "aeiou"

        consonants = [letter for letter in string.ascii_lowercase if letter not in vowels]

        print("".join(consonants))



class CodingProblems2:
    def reverse_string(self):
        string = "text"

        string = string[::-1]

        print(string)

    def find_largest(self):
        arr = [1,2,9,5,3]

        _max = arr[0]

        for i in arr:
            if i > _max:
                _max = i

        print(_max)

    def check_palindrome(self):
        string = "text"

        reversed_string = string[::-1]

        if string == reversed_string:
            print(f"{string} is Palindrome")
        else:
            print(f"{string} is not palindrome")

    def count_frequency_char_in_str(self):
        string = "jjjoos"

        _string_dic = {}

        for c in string:
            if c in _string_dic:
                _string_dic[c] += 1
            else:
                _string_dic[c] = 1

        print(_string_dic)

    def find_first_non_repeating_char(self):
        string = "jjqmsjssaqqq"

        char_count = {}

        for c in string:
            if c in char_count:
                char_count[c] += 1
            else:
                char_count[c] = 1

        s = ''

        for k,v in char_count.items():
            if v == 1:
                s = k
                break

        print(f"the first non repeating character is {s}")

    def longest_substring_without_repeating_character(self):
        s = "abcabcbb"

        char_set = set()  # To store unique characters
        left = 0  # Left pointer of the window
        max_length = 0  # To store the max length

        for right in range(len(s)):  # Right pointer moves through the string
            while s[right] in char_set:  # If duplicate found, shrink window
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])  # Add unique character to the set
            max_length = max(max_length, right - left + 1)  # Update max length


        print(max_length)

    def find_missing_num(self):
        arr = [1,2,3,4,5,6,7,8,9,10,11,13]
        n = len(arr) + 1

        expected_sum = n * (n + 1) // 2

        actual_sum = sum(arr)

        print(f"The missing numbers is {expected_sum - actual_sum}")

    def relation_to_josuan(self, name):
        family_tree = {
            "father": "Darth Vader",
            "sister": "Leia",
            "brother in law": "Han",
            "R2D2": "droid"
        }

        relation = next((k for k, v in family_tree.items() if v == name),None)

        print(f"{name}, I am your {relation}")

    def get_median_of_two_sorted_array(self,arr):
        n = len(arr)

        if n % 2 == 0:
            mid1 = n // 2 - 1
            mid2 = n // 2
            return (arr[mid1] + arr[mid2]) / 2
        else:
            mid = n // 2
            return (arr[mid - 1] + arr[mid]) / 2

    def two_sum_problem(self, arr, target):
        n = len(arr)
        x, y = -1, -1
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] + arr[j] == target:
                    x, y = i, j
                    break
            if x != -1:
                break

        return [x,y]


problem2 = CodingProblems2()

result = problem2.two_sum_problem([2,2,3,4,2,3,1,3,4],8)

print(result)