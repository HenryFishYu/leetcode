from typing import Optional, List

from basic_class import TreeNode


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        res = []
        temp = []

        def dfs(node: Optional[TreeNode],targetSum: int):
            if not node:
                return

            if not node.left and not node.right:
                if targetSum-node.val==0:
                    temp.append(node.val)
                    res.append(temp.copy())
                    temp.pop()
                return

            temp.append(node.val)
            dfs(node.left,targetSum-node.val)
            temp.pop()

            temp.append(node.val)
            dfs(node.right,targetSum-node.val)
            temp.pop()

        dfs(root,targetSum)
        return res


