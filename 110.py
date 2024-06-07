from typing import Optional

from basic_class import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def height(root) -> (int, bool):
            if not root:
                return 0,True
            left, left_b = height(root.left)
            right, right_b = height(root.right)
            if not (left_b and right_b) or abs(left - right) > 1:
                return 0, False
            return max(left, right) + 1, True

        left, left_b = height(root.left)
        right, right_b = height(root.right)
        if not (left_b and right_b) or abs(left - right) > 1:
            return False
        return True


head = TreeNode(1, left=TreeNode(2, left=TreeNode(3, left=TreeNode(4), right=TreeNode(4)), right=TreeNode(3)),
                right=TreeNode(2))
res = Solution().isBalanced(head)
print(res)
