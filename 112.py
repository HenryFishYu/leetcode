from typing import Optional

from basic_class import TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if root.val==targetSum and not root.left and not root.right:
            return True


        left = root.left
        if left:
            left.val += root.val

        right = root.right
        if right:
            right.val += root.val

        return self.hasPathSum(left,targetSum) or self.hasPathSum(right,targetSum)