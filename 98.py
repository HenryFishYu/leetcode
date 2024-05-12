from typing import Optional

from basic_class import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev, res = None, True

        def dfs(node: Optional[TreeNode]):
            if not node:
                return

            dfs(node.left)
            nonlocal prev, res
            if prev:
                if not node.val > prev.val:
                    res = False
                    return
            prev = node
            dfs(node.right)

        dfs(root)
        return res
