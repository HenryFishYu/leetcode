from basic_class import Node


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map = {}
        current = head
        while current:
            map[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            new = map[current]
            if current.next:
                new.next = map[current.next]
            if current.random:
                new.random = map[current.random]
            current = current.next
        return map[head]