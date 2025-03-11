import math

class CodingProblems:
    statement = "Coding problems that I solve during my practice for coding competition"

    def __str__(self):
        return self.statement

    def __repr__(self):
        return self.statement

    @staticmethod
    def isPrimeNumber(n) -> str:
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

        return f"{n} is Prime number" if is_prime else f"{n} is not Prime number"

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

print(CodingProblems.findNthFibonacciNumber(6))