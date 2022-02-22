"""

"""


class Solution:
    a = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root is None:
            return
        self.bstToGst(root.right)
        self.a += root.val
        root.val = self.a
        self.bstToGst(root.left)
        return root
