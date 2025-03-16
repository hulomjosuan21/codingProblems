from itertools import count, repeat, cycle, accumulate, chain, compress, pairwise, product, combinations

# counter = count(1,1)
#
# for i in counter:
#     print(i)
#     if i == 100:
#         break

# |---------------------------------------|

# repeater = repeat("Josuan",100)
#
# for name in repeater:
#     print(name)

# repeater = repeat("Josuan",10)
#
# print(list(repeater))

# |---------------------------------------|

# cycler = cycle([1,2,3])
#
# for i in range(50):
#     print(next(cycler),end=" ")

# |---------------------------------------|

# nums = [1,2,3,4,5,6,7,8,9,10]
#
# print(list(accumulate(nums)))

# |---------------------------------------|

# nums1 = [1,2,3]
# nums2 = [4,5,6]
#
# chained = chain(nums1,nums2)
# print(list(chained))

# |---------------------------------------|

# chained = chain.from_iterable([[1,2,3],[4,5,6],[7,8,9]])
#
# print(list(chained))

# |---------------------------------------|

# compressed = compress([[1,2,3],['A','B','C'],[True,True,True]], [1,1,1])
#
# print(list(compressed))

# |---------------------------------------|

# paired = pairwise([1,2,3,4,5,6,7,8,9,10])
#
# print(list(paired))

# |---------------------------------------|

# result = product([1,2,3],['A','B','C'])
#
# print(list(result))

# |---------------------------------------|

# result = combinations(['A','B','C'],2)
#
# print(list(result))

# |---------------------------------------|
