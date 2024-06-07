from typing import Optional

from basic_class import TreeNode


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def depth(root):
            if not root:
                return 10 ** 5
            if not root.left and not root.right:
                return 1
            return min(depth(root.left), depth(root.right)) + 1

        return depth(root)
