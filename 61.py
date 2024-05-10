# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from basic_class import ListNode


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(None,head)
        slow = dummy
        fast = dummy
        first = head
        current = head
        count = 1
        while current.next:
            count+=1
            current = current.next

        k = k%count
        if k==0:
            return dummy.next

        for _ in range(k+1):
            slow = slow.next

        while slow:
            slow = slow.next
            fast = fast.next

        dummy.next = fast.next
        fast.next = None
        current.next = first

        return dummy.next



