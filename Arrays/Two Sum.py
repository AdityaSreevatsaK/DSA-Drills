from typing import Optional, Tuple


def two_sum(nums: list, target: int) -> Optional[Tuple[int, int]]:
    viewed = {}
    for index, value in enumerate(nums):
        requirement = target - value
        if requirement in viewed:
            match = nums.index(requirement), index
            print(f"Match found: {match}")
            return match
        viewed[value] = requirement
    print("Match not found.")
    return None


if __name__ == "__main__":
    print(f"two_sum([2,7,11,15], 9) -> {two_sum([2, 7, 11, 15], 9)} ")
