import math
# num = input("Input number: ")
# number = int(num)

# sum all the digit in the number
# num = int(input("Input number: "))
# sum = 0
# while num > 0:
#     digit = num % 10
#     sum += digit
#     num //= 10
#
# print(sum)

# arr = [1,3,2,4]
#
# for i in range(len(arr) -1, 0, -1):
#     for j in range(i):
#         if arr[j] > arr[j+1]:
#             temp = arr[j]
#             arr[j] = arr[j+1]
#             arr[j+1] = temp
#
# print(arr)

# Check if Palindrome number
# temp = int(num)
# a = []
# b = []
# while temp > 0:
#     digit = temp % 10
#     a.append(digit)
#     temp //= 10
#
# for n in num:
#     b.append(int(n))
#
#
# result = "Yes" if a == b else "No"

# result = 0
# for i in range(number-1,0,-1):
#     if i+1 == number:
#         result = number * i
#     else:
#         result *= i
#
# print(result)

# frequency = {}
# while number > 0:
#     digit = number % 10
#     if digit in frequency:
#         frequency[digit] += 1
#     else:
#         frequency[digit] = 1
#     number //= 10
#
# most_common_digit = max(frequency, key=frequency.get)
# print(f"Most commot digit {most_common_digit}")

# balance ()
# text = "(((())))"
#
# mid = len(text) // 2
#
# open = text[:mid]
# close = text[mid:]
#
# result = "Yes"
#
# for c in open:
#     if c != '(':
#         result = "No"
#
# for c in close:
#     if c != ')':
#         result = "No"
#
# print(result)
#
# numbers = [1,2,3,4,5,6,7,8,9,10,11,13,14,15]
# n = numbers[len(numbers)-1]
# expected_sum = n * (n + 1) // 2
#
# actual_sum = sum(numbers)
# print(expected_sum)
# print(actual_sum)
#
# result = expected_sum - actual_sum
#
# print(result)

# reverse string
# text = "Josuan"
#
# reversed_string = ''
#
# for i in range(len(text)-1,-1,-1):
#     reversed_string += text[i]
#
# print(reversed_string)

# text = "josuan"
#
# reversed_string = ''
#
# for i in range(len(text)-1,-1,-1):
#     reversed_string += text[i]
#
# print("Yes" if text == reversed_string else "No")

# arr_of_nums = [5,2,8,7,5]
#
# _max = arr_of_nums[0]
# _min = arr_of_nums[0]
#
# for i in range(len(arr_of_nums)-1):
#     if arr_of_nums[i+1] > _max:
#         _max = arr_of_nums[i+1]
#
#     if arr_of_nums[i+1] < _min:
#         _min = arr_of_nums[i+1]
#
#
# print(_min)

num = 7

# x = math.sqrt(num)
# x = (num ** 0.5)

x = 5 // 2
print(int(x))