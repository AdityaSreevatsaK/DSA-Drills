from typing import List


def max_subarray_sum(nums: List[int]) -> int:
    max_sum = float("-inf")
    current = 0
    for value in nums:
        current = max(value, current + value)
        max_sum = max(max_sum, current)
    return max_sum


if __name__ == "__main__":
    maximum_sum = max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(f"max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) -> {maximum_sum}")
