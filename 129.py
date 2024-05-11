from typing import Optional

from basic_class import TreeNode


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return root.val

        if root.left:
            root.left.val += root.val*10

        if root.right:
            root.right.val += root.val*10

        return self.sumNumbers(root.left) + self.sumNumbers(root.right)