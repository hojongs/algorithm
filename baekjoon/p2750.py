# https://www.acmicpc.net/problem/2750
import sys
from typing import List


def f(nums: List[int]) -> List[int]:
    return sorted(nums)


# print(f([5, 4, 3, 2, 1]))
# print(f([1, 3, 2, 5, 4]))

n = int(sys.stdin.readline())
nums = [0] * n
for i in range(n):
    nums[i] = int(sys.stdin.readline())

nums2 = f(nums)

output = ''
for num in nums2:
    output += str(num) + '\n'
sys.stdout.write(output)
