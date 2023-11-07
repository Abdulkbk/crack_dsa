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


def count_rotations2(nums):
    posiiton = 0

    while posiiton < len(nums):
        if posiiton > 0 and nums[posiiton] < nums[posiiton - 1]:
            return posiiton
        posiiton += 1
    return posiiton


if __name__ == "__main__":
    crack = count_rotations([3, 4, 5, 1, 2])
    print(f"Numbers of rotations: {crack}")
    crack2 = count_rotations([4, 5, 6, 7, 1, 2, 3])
    print(f"Numbers of rotations: {crack2}")
