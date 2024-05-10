# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from basic_class import ListNode


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_dummy = ListNode(None)
        greater_dummy = ListNode(None)
        less = less_dummy
        greater = greater_dummy

        while head:
            if head.val<x:
                less_dummy.next = head
                less_dummy = less_dummy.next
            else:
                greater_dummy.next = head
                greater_dummy = greater_dummy.next
            head = head.next

        greater_dummy.next = None

        less_dummy.next = greater.next
        return less.next