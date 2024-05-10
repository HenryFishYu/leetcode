# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from basic_class import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None,head)
        current = dummy
        tempVal = None
        while current.next and current.next.next:
            if current.next.val == current.next.next.val:
                tempVal = current.next.val
                current.next = current.next.next.next
                continue
            if current.next.val == tempVal:
                current.next = current.next.next
                continue
            if current.next.val != tempVal:
                current = current.next
                tempVal = None

        if current.next and current.next.val == tempVal:
            current.next=None
        return dummy.next


