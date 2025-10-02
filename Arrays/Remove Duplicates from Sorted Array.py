from typing import List


def remove_duplicates_from_sorted_array(nums: List[int]) -> int:
    if not nums:
        return 0

    next_pos = 1
    for value in range(1, len(nums)):
        if nums[value] != nums[value - 1]:
            nums[next_pos] = nums[value]
            next_pos += 1
    return next_pos


if __name__ == "__main__":
    cleaned_list = remove_duplicates_from_sorted_array([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    print(f"remove_duplicates_from_sorted_array([0,0,1,1,1,2,2,3,3,4]) -> {cleaned_list}")
