from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        m_index = m-1
        n_index = n-1
        k = n+m-1
        while n_index>=0:
            if (m_index>=0) & (nums1[m_index]>nums2[n_index]):
                nums1[k] = nums1[m_index]
                m_index -= 1
            else:
                nums1[k] = nums2[n_index]
                n_index -= 1
            k -= 1
