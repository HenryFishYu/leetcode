from typing import Optional

from basic_class import ListNode


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(None,head)
        left_previous,current = dummy,dummy.next

        for i in range(left-1):
            left_previous,current = left_previous.next,current.next

        previous = None
        for i in range(right-left+1):
            next = current.next
            current.next = previous
            previous = current
            current = next

        left_previous.next.next = current
        left_previous.next = previous
        return dummy.next



