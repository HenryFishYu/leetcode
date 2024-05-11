from collections import deque

from basic_class import Node


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        current = root
        while current:
            dummy = Node(None,current)
            temp = dummy
            while current:
                if current.left:
                    dummy.next = current.left
                    dummy = dummy.next
                elif current.right:
                    dummy.next = current.right
                    dummy = dummy.next
                current = current.next
            current = temp.next
        return  root



