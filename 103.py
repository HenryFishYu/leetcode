from collections import deque
from typing import Optional, List

from basic_class import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = [root]
        while q:
            level = []
            for node in reversed[q]:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            if level:
                res.append([node.val for node in q])
            q = level
        return res

