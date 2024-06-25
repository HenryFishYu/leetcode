from typing import List, Optional

from basic_class import TreeNode


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None

        inorder_index_map = {v:i for i,v in enumerate(inorder)}

        def helper(l,r):
            if l>r:
                return None
            root = TreeNode(postorder.pop())
            index = inorder_index_map[root.val]
            root.right = helper(index+1,r)
            root.left = helper(l,index-1)
            return root

        return helper(0,len(inorder)-1)

Solution().buildTree([9,3,15,20,7],[9,15,7,20,3])