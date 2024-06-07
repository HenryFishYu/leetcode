from typing import Optional

from basic_class import ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None,head)
        temp = dummy

        while temp.next and temp.next.next:
            next_pair = temp.next.next.next
            temp.next.next.next = temp.next
            temp.next = temp.next.next
            temp.next.next.next = next_pair
            temp = temp.next.next
        return dummy.next
