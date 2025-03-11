import math

class CodingProblems:
    def __repr__(self):
        return "Coding problems that I solve during my practice for coding competition"

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


result = CodingProblems.isPrimeNumber(7)

print(result)