# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from basic_class import TreeNode


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def dfs(node: Optional[TreeNode])->int:

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            total_max = max(node.val,node.val+left,node.val+right,node.val+left+right)
            res[0] = max(total_max,res[0])
            partial_max = max(node.val,node.val+left,node.val+right)
            return partial_max

        dfs(root)

        return res[0]