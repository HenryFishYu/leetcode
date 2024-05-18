from typing import Optional

from basic_class import ListNode


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None,head)
        temp = dummy
        arr = []
        while(head):
            arr.append(head)
            head = head.next

        arr.sort(key=lambda head:head.val)

        for item in arr:
            temp.next = item
            temp = item
        temp.next = None
        return dummy.next