# Day 2 Solutions - Niyati Jha

# 1. Sum of All Even Numbers
def sum_of_even_numbers(nums):
    return sum(num for num in nums if num % 2 == 0)

# 2. Find First and Last Element
def first_and_last(nums):
    if not nums:
        return None, None
    return nums[0], nums[-1]

# 3. Check if Two Arrays are Equal
def arrays_equal(nums1, nums2):
    from collections import Counter
    return Counter(nums1) == Counter(nums2)


# Example Test Cases
if __name__ == "__main__":
    print("1. Sum of Even Numbers")
    print(sum_of_even_numbers([1, 2, 3, 4, 5]))  # Output: 6
    print(sum_of_even_numbers([10, 15, 20]))     # Output: 30
    print(sum_of_even_numbers([1, 3, 5]))        # Output: 0

    print("\n2. First and Last Elements")
    print(first_and_last([1, 2, 3, 4]))          # Output: (1, 4)
    print(first_and_last([7]))                   # Output: (7, 7)
    print(first_and_last([5, 9, 2]))             # Output: (5, 2)

    print("\n3. Arrays Equal?")
    print(arrays_equal([1, 2, 3, 4], [4, 3, 2, 1]))    # True
    print(arrays_equal([1, 2, 2, 3], [1, 2, 3, 3]))    # False
    print(arrays_equal([1, 2, 3], [1, 2, 3, 4]))
