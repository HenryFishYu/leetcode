from typing import List, Optional

from basic_class import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = preorder[0]
        index = inorder.index(root)

        node = TreeNode(root)
        node.left = self.buildTree(preorder[1:index+1],inorder[:index])
        node.right = self.buildTree(preorder[index+1:],inorder[index+1:])
        return node