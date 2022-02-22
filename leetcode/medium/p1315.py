"""

"""


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if root is None:
            return 0

        result = 0
        if root.val % 2 == 0:
            if root.left is not None:
                if root.left.left is not None:
                    result += root.left.left.val
                if root.left.right is not None:
                    result += root.left.right.val
            if root.right is not None:
                if root.right.left is not None:
                    result += root.right.left.val
                if root.right.right is not None:
                    result += root.right.right.val
        result += self.sumEvenGrandparent(root.left)
        result += self.sumEvenGrandparent(root.right)
        return result
