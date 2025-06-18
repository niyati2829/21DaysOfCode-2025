
# 1. K-Frequency Element Sum
# Given an array and integer k, return the sum of all distinct elements
# that appear exactly k times in the array.

def k_frequency_sum(nums, k):
    from collections import Counter
    freq = Counter(nums)
    total = 0

    for num, count in freq.items():
        if count == k:
            total += num

    return total

# Test Cases
print("Q1: K-Frequency Element Sum")
print(k_frequency_sum([2, 3, 9, 9], 1))  # Output: 5
print(k_frequency_sum([1, 8, 8, 8, 5, 6, 2], 3))  # Output: 8


# 2. Check for Duplicates

# Return True if any number appears more than once, else False

def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Test Cases
print("\nQ2: Check for Duplicates")
print(contains_duplicate([1, 2, 3, 4]))  # Output: False
print(contains_duplicate([1, 2, 3, 2]))  # Output: True
print(contains_duplicate([5, 5, 5]))     # Output: True


# 3. Find the Second Largest Element

# Return second largest unique element in the array. If it doesn't exist, return -1

def second_largest(nums):
    unique_nums = list(set(nums))  # Remove duplicates
    if len(unique_nums) < 2:
        return -1
    unique_nums.sort(reverse=True)
    return unique_nums[1]

# Test Cases
print("\nQ3: Second Largest Unique Element")
print(second_largest([10, 20, 30, 40]))  # Output: 30
print(second_largest([5, 5, 5]))         # Output: -1
print(second_largest([3, 2, 1]))         # Output: 2
