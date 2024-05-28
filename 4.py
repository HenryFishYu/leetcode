from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            A,B = nums1,nums2
        else:
            A,B = nums2,nums1

        total = len(nums1) + len(nums2)
        half = total // 2
        l,r = 0, len(A)-1

        while True:
            A_mid = (l+r)//2
            B_mid = half-A_mid-2
            A_left = A[A_mid] if A_mid>=0 else float("-inf")
            A_right = A[A_mid+1] if A_mid+1<len(A) else float("inf")
            B_left = B[B_mid] if B_mid>=0 else float("-inf")
            B_right = B[B_mid+1] if B_mid+1<len(B) else float("inf")

            if A_left<=B_right and B_left<=A_right:
                if total%2==0:
                    return (max(A_left,B_left)+min(A_right,B_right))/2
                else:
                    return min(A_right,B_right)

            if A_left > B_right:
                r = A_mid-1
                continue

            if A_right < B_left:
                l = A_mid + 1
                continue
        return -1


print(Solution().findMedianSortedArrays([1,3],[2]))