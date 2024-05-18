from typing import List, Optional

from basic_class import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==0:
            return None
        if len(nums)==1:
            return TreeNode(val=nums[0])

        mid_index = len(nums)//2
        return TreeNode(val=nums[mid_index],left=self.sortedArrayToBST(nums[:mid_index]),right=self.sortedArrayToBST(nums[mid_index+1:]))