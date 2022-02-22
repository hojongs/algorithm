"""

"""
from typing import List, Optional

from tree_node import TreeNode, convert_tree_node_as_list


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self._f(nums, 0, len(nums))

    def _f(self, nums: List[int], start: int, endExclusive: int) -> Optional[TreeNode]:
        if endExclusive - start <= 0:
            return None

        m = max([nums[i] for i in range(start, endExclusive)])
        i = nums.index(m)
        root = TreeNode(m)
        root.left = self._f(nums, start, i)
        root.right = self._f(nums, i + 1, endExclusive)
        return root


if __name__ == '__main__':
    print(
        convert_tree_node_as_list(
            Solution().constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
        )
    )
