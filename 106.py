from typing import List, Optional

from basic_class import TreeNode


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder or not inorder:
            return None

        root = postorder[-1]
        index = inorder.index(root)

        node = TreeNode(root)
        node.left = self.buildTree(postorder[:index],inorder[:index])
        node.right = self.buildTree(inorder[index+1:],postorder[index:-1])
        return node

Solution().buildTree([9,3,15,20,7],[9,15,7,20,3])