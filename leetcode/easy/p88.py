"""
88. Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1, i2, i3 = m - 1, n - 1, m + n - 1
        while True:
            if i1 == -1:
                while i2 >= 0:
                    nums1[i3] = nums2[i2]
                    i3 -= 1
                    i2 -= 1

            if i3 == -1 or i2 == -1:
                return

            if nums1[i1] >= nums2[i2]:
                nums1[i3] = nums1[i1]
                i1 -= 1
            else:
                nums1[i3] = nums2[i2]
                i2 -= 1
            i3 -= 1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    Solution().merge(nums1, 3, [2, 5, 6], 3)
    print(nums1)
    nums1 = [2, 0]
    Solution().merge(nums1, 1, [1], 1)
    print(nums1)
