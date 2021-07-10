# https://www.acmicpc.net/problem/2750
from typing import List


def f(nums: List[int]) -> List[int]:
    nums2 = []
    while True:
        if len(nums) == 0:
            break

        i = 1
        min_i = 0
        while True:
            if i >= len(nums):
                break

            if nums[min_i] >= nums[i]:
                min_i = i
            i += 1
        nums2.append(nums.pop(min_i))
    return nums2


# print(f([5, 4, 3, 2, 1]))
# print(f([1, 3, 2, 5, 4]))

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

nums2 = f(nums)

for num in nums2:
    print(num)
