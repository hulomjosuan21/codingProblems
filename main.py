def get_all_digits(num) -> [int]:
    stack = []
    while num > 0:
        stack.append(num%10)
        num //= 10

    return stack[::-1]

print(get_all_digits(100))