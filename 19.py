from typing import Optional

from basic_class import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(None,head)
        slow = head
        fast = head

        for _ in range(n+1):
            slow = slow.next

        while slow:
            slow = slow.next
            fast = fast.next

        fast.next = fast.next.next
        return dummy.next
