import queue
from typing import Optional, List

from basic_class import ListNode


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if (lists is None) | (len(lists) == 0):
            return None
        priority_queue: queue.PriorityQueue[(int, int, ListNode)] = queue.PriorityQueue()
        for i, listNode in enumerate(lists):
            tempNode = listNode
            while tempNode:
                priority_queue.put((tempNode.val, i, tempNode))
                tempNode = tempNode.next

        result_node = priority_queue.get()
        while not priority_queue.empty():
            result_node.next = priority_queue.get()[2]
            result_node = result_node.next

        return result_node

if __name__ == "__main__":
    Solution().mergeKLists([[]])