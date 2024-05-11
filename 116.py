from basic_class import Node


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        next,current = root.left,root

        while current and next:
            current.left.next = current.right
            if current.next:
                current.right.next = current.next.left

            current = current.next

            if not current:
                current = next
                next = current.left

        return root

