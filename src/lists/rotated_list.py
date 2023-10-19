"""
Given a rotated sorted list for n numbers, find the number of rotation

Input: nums -> [1, 2, 3, 4, 5] -> [3, 4, 5, 1, 2]

Output: 3
"""


def count_rotations(nums):
    arr = []
    for i, j in enumerate(nums):
        if i + 1 < len(nums):
            if j > nums[i + 1]:
                arr = nums[: i + 1]
        else:
            return len(arr)
    return len(arr)
