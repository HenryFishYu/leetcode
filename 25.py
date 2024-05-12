from typing import Optional

from basic_class import ListNode


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_arr(arr: [], k: int):
            length = len(arr)
            for i in range(0, length, k):
                if i + k > length:
                    continue
                else:
                    arr[i:i + k] = reversed(arr[i:i + k])
        arr = []
        while head:
            arr.append(head)
            head = head.next
        reverse_arr(arr,k)
        dummy = ListNode(None)
        res = dummy
        for node in arr:
            dummy.next = node
            dummy = dummy.next

        dummy.next = None

        return res.next