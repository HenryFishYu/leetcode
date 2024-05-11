from typing import Optional

from basic_class import TreeNode


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev,res = None, 100000

        def dfs(node: Optional[TreeNode]):
            if not node:
                return

            dfs(node.left)
            nonlocal prev,res
            if prev:
                res = min(res,node.val-prev.val)
            prev = node
            dfs(node.right)

        dfs(root)
        return res

