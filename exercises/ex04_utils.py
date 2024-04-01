"""EX04 List Utility Functions."""

__author__ = "730712233"


def all(nums: list[int], number: int) -> bool:
    """Determines whether all numbers in a list are the same as a given number."""
    all_counter: int = 1
    if len(nums) == 0:
        return False
    while all_counter <= len(nums):
        if nums[all_counter - 1] != number:
            return False
        else:
            all_counter += 1
    return True


def max(nums: list[int]) -> int:
    """Determines the maximum value of a list."""
    if len(nums) == 0:
        raise ValueError("max() arg is an empty List")
    max_counter: int = 1
    max_number: int = nums[0]
    while max_counter <= len(nums):
        if nums[max_counter - 1] > max_number:
            max_number = nums[max_counter - 1]
            max_counter += 1
        else:
            max_counter += 1
    return max_number


def is_equal(nums1: list[int], nums2: list[int]) -> bool:
    """Determines if two lists are the same as each other."""
    is_equal_counter: int = 1
    if len(nums1) != len(nums2):
        return False
    if nums1 == [] and nums2 == [0]:
        return True
    while is_equal_counter <= len(nums1):
        if nums1[is_equal_counter - 1] != nums2[is_equal_counter - 1]:
            return False
        else:
            is_equal_counter += 1
    return True


def extend(nums1: list[int], nums2: list[int]) -> None:
    """Mutates the first list by adding the second list's values to it."""
    nums2_counter: int = 1
    while nums2_counter <= len(nums2):
        nums1.append(nums2[nums2_counter - 1])
        nums2_counter += 1
    return None