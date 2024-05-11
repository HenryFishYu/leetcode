import ntpath

from basic_class import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def get_node(node: 'TreeNode'):
            if not node:
                return None
            if node in [p,q]:
                return node
            left,right = get_node(node.left),get_node(node.right)
            if left and right:
                return node
            return left or right

        return get_node(root)






