# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from basic_class import ListNode, TreeNode


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        if not head.next.next:
            return TreeNode(head.val,right=TreeNode(head.next.val))
        dummy = ListNode(None,head)
        fast = dummy
        slow = dummy
        prev = dummy
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None
        treeNode = TreeNode(slow.val)
        left = self.sortedListToBST(head)
        right = self.sortedListToBST(slow.next)
        treeNode.left = left
        treeNode.right = right
        return treeNode

fifth = ListNode(9)
fourth = ListNode(5,fifth)
third = ListNode(0,fourth)
second = ListNode(-3,third)
first = ListNode(10,second)

res = Solution().sortedListToBST(first)
print(res)


