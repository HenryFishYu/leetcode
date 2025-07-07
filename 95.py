from typing import List, Optional

from basic_class import TreeNode


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        memo = {}
        def helper(start: int, end: int) -> List[Optional[TreeNode]]:
            if start>end:
                return [None]
            if start == end:
                return [TreeNode(start)]
            if (start,end) in memo:
                return memo[(start,end)]

            res = []
            for i in range(start,end+1):
                left_trees = helper(start,i-1)
                right_trees = helper(i+1,end)
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        res.append(root)
            memo[(start,end)] = res
            return res
        return helper(1,n)

