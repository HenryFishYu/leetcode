from typing import Optional

from basic_class import TreeNode


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def dfs(node: Optional[TreeNode])->TreeNode:
            if not node:
                return None
            left_tail = dfs(node.left)
            right_tail = dfs(node.right)

            if node.left:
                left_tail.right = node.right
                node.right = node.left
                node.left = None
            last = right_tail or left_tail or node
            return last

        dfs(root)