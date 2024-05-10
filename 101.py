from typing import Optional

from basic_class import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(left: Optional[TreeNode],right: Optional[TreeNode]):
            if not left and not right:
                return True

            if not left or not right:
                return False

            return left.val==right.val and isMirror(left.left,right.right) and isMirror(left.right,right.left)

        if not root:
            return True

        return isMirror(root.left,root.right)