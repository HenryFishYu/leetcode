import heapq
import queue
from typing import Optional, List

from basic_class import ListNode


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(None)
        temp = dummy
        queue = []
        count = 0
        for listNode in lists:
            if listNode:
                heapq.heappush(queue,(listNode.val,count,listNode))
                count += 1

        while len(queue)>0:
            _,_,first = heapq.heappop(queue)
            temp.next = first
            temp = temp.next
            if first.next:
                heapq.heappush(queue,(first.next.val,count,first.next))
                count += 1

        return dummy.next