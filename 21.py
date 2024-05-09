import heapq
import queue
from typing import Optional

from basic_class import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        heap = []
        head = ListNode(None)
        current = head

        if list1:
            heapq.heappush(heap, (list1.val, 0, list1))
        if list2:
            heapq.heappush(heap, (list2.val, 1, list2))
        while heap:
            val, weight, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if current.next:
                heapq.heappush(heap, (current.next.val, weight, current.next))

        return head.next


