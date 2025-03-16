import math

class CodingProblems:
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



strings = ["interstellar", "internet", "interval"]
result = CodingProblems.findLongestCommonPrefix(strings)

print(result)



