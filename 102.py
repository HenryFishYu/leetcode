from typing import Optional, List

from basic_class import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        temp = [root]
        res = []
        count = 0
        while temp:
            new_temp = []
            for node in temp:
                if node.left:
                    new_temp.append(node.left)
                if node.right:
                    new_temp.append(node.right)
            if count % 2 == 0:
                res.append([node.val for node in temp])
            else:
                res.append([node.val for node in reversed(temp)])
            count += 1
            temp = new_temp
        return res

