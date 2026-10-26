# 1. Sorting with an Even Number of Swaps (1 Point)
# Given an array of numbers (a_1, a_2, \ldots, a_n), you can swap any two adjacent elements in a single operation.
# Is it possible to sort the array in non-decreasing order such that each element participates in an even number of swaps?
# Determine the answer in (O(n \log n)) time.
# Note: The array may contain duplicate values.

# def can_sort(a):
#     b = sorted(a)
#     original_even = sorted(a[::2])
#     sorted_even = sorted(b[::2])
#     return original_even == sorted_even
# print(can_sort([2, 1, 1, 2]))  
# print(can_sort([2, 1]))        
# print(can_sort([1, 1, 1]))     



# 2. Sorting in O(n + √k) Time (1 Point)
# Given an array of numbers (a_1, a_2, \ldots, a_n), where
# [a_i \in {0,1,\ldots,k}]
# for every (i).
# Sort the array in (O(n+\sqrt{k})) time.

# from math import isqrt
# def radix_sort(a, k):
#     base = isqrt(k) + 1
#     def counting_sort(arr, place):
#         count = [0] * base
#         for num in arr:
#             digit = (num // place) % base
#             count[digit] += 1
#         for i in range(1, base):
#             count[i] += count[i - 1]
#         result = [0] * len(arr)
#         for num in reversed(arr):
#             digit = (num // place) % base
#             count[digit] -= 1
#             result[count[digit]] = num
#         return result
#     a = counting_sort(a, 1)
#     a = counting_sort(a, base)
#     return a
# a = [7, 3, 12, 1, 10, 3]
# k = 15
# print(radix_sort(a, k))



# 3. Stability of Sorting Algorithms (1 Point)
# Investigate Merge Sort and Quick Sort with respect to stability.
# Answer the following questions:
# Are their classical implementations stable?
# Is it possible to modify their implementations to make them stable?

# QUICK SORT - STABLE
# students = [
#     (20, "Anna"),
#     (18, "Aram"),
#     (20, "David"),
#     (18, "Mariam")
# ]
# def stable_quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2][0]
#     less = []
#     equal = []
#     greater = []
#     for item in arr:
#         if item[0] < pivot:
#             less.append(item)
#         elif item[0] == pivot:
#             equal.append(item)
#         else:
#             greater.append(item)
#     return (
#         stable_quick_sort(less)
#         + equal
#         + stable_quick_sort(greater)
#     )
# print(stable_quick_sort(students))

# MERGE SORT- STABLE
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i][0] <= right[j][0]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result
# students = [
#     (20, "Anna"),
#     (18, "Aram"),
#     (20, "David"),
#     (18, "Mariam")
# ]
# print(merge_sort(students))



# 4. Maximum Gap Between Consecutive Order Statistics (2 Points)
# Given an array of integers (a_1, a_2, \ldots, a_n), find
# [\max_{i=1}^{n-1}\left(a_{(i+1)}-a_{(i)}\right)]
# where (a_{(k)}) denotes the k-th order statistic (the k-th smallest element).
# Required time complexity: (O(n)).

# def maximum_gap(a):
#     n = len(a)
#     if n < 2:
#         return 0
#     min_val = min(a)
#     max_val = max(a)
#     if min_val == max_val:
#         return 0
#     size = (max_val - min_val + n - 2) // (n - 1)
#     count = (max_val - min_val) // size + 1
#     buckets_min = [None] * count
#     buckets_max = [None] * count
#     for num in a:
#         index = (num - min_val) // size
#         if buckets_min[index] is None:
#             buckets_min[index] = num
#             buckets_max[index] = num
#         else:
#             buckets_min[index] = min(buckets_min[index], num)
#             buckets_max[index] = max(buckets_max[index], num)
#     max_gap = 0
#     prev_max = None
#     for i in range(count):
#         if buckets_min[i] is None:
#             continue
#         if prev_max is not None:
#             gap = buckets_min[i] - prev_max
#             max_gap = max(max_gap, gap)
#         prev_max = buckets_max[i]
#     return max_gap
# a = [3, 6, 9, 1, 20]
# print(maximum_gap(a))



# 5. Derandomised Quick Select with Different Group Sizes (3 Points)
# In the linear-time algorithm for finding the k-th order statistic (Derandomised Quick Select), the entire array is divided into groups of 5 elements.
# What happens if, instead, the array is divided into groups of (2m+1) elements, where (m) is a constant?
# Determine the time complexity of the algorithm in this case.

# def kth_smallest(a, k, group_size=5):
#     if group_size < 3 or group_size % 2 == 0:
#         raise ValueError("Group size must be odd and >= 3")
#     if not 0 <= k < len(a):
#         raise IndexError("Invalid k")
#     def select(arr, index):
#         if len(arr) <= group_size:
#             return sorted(arr)[index]
#         medians = []
#         for start in range(0, len(arr), group_size):
#             group = sorted(arr[start:start + group_size])
#             medians.append(group[len(group) // 2])
#         pivot = select(medians, len(medians) // 2)
#         less = [x for x in arr if x < pivot]
#         equal = [x for x in arr if x == pivot]
#         greater = [x for x in arr if x > pivot]
#         if index < len(less):
#             return select(less, index)
#         if index < len(less) + len(equal):
#             return pivot
#         return select(
#             greater,
#             index - len(less) - len(equal)
#         )
#     return select(a, k)
# a = [12, 3, 5, 7, 4, 19, 26, 11, 2, 8, 17, 6, 9, 14, 1]
# print(kth_smallest(a, 10, 5))
# print(kth_smallest(a, 10, 3))



# 6.Multiple Order Statistics Queries (3 Points)
# Suppose you are given an array of length (n) and (m \leq n) queries for finding order statistics.
# Design a deterministic algorithm that answers all queries in
# [O(n\log m)] time.

# def select_deterministic(values, k):
#     if len(values) <= 5:
#         return sorted(values)[k]
#     medians = []
#     for i in range(0, len(values), 5):
#         group = sorted(values[i:i + 5])
#         medians.append(group[len(group) // 2])
#     pivot = select_deterministic(
#         medians, len(medians) // 2
#     )
#     less = []
#     greater = []
#     equal_count = 0
#     for x in values:
#         if x < pivot:
#             less.append(x)
#         elif x > pivot:
#             greater.append(x)
#         else:
#             equal_count += 1
#     if k < len(less):
#         return select_deterministic(less, k)
#     if k < len(less) + equal_count:
#         return pivot
#     return select_deterministic(
#         greater, k - len(less) - equal_count
#     )
# def answer_order_statistics(a, queries):
#     n = len(a)
#     if any(k < 1 or k > n for k in queries):
#         raise ValueError("Invalid rank")
#     results = [None] * len(queries)
#     requested = sorted(
#         [(k - 1, i) for i, k in enumerate(queries)]
#     )
#     def solve(values, jobs):
#         if not jobs:
#             return
#         rank = jobs[len(jobs) // 2][0]
#         pivot = select_deterministic(values, rank)
#         less = []
#         greater = []
#         equal_count = 0
#         for x in values:
#             if x < pivot:
#                 less.append(x)
#             elif x > pivot:
#                 greater.append(x)
#             else:
#                 equal_count += 1
#         left_jobs = []
#         right_jobs = []
#         low_count = len(less)
#         high_start = low_count + equal_count
#         for k, position in jobs:
#             if k < low_count:
#                 left_jobs.append((k, position))
#             elif k < high_start:
#                 results[position] = pivot
#             else:
#                 right_jobs.append(
#                     (k - high_start, position)
#                 )
#         solve(less, left_jobs)
#         solve(greater, right_jobs)
#     solve(a, requested)
#     return results
# a = [8, 1, 5, 2, 10, 4, 7, 3]
# queries = [1, 4, 6, 8]
# print(answer_order_statistics(a, queries))