from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        leftIndex = 0
        rightIndex = len(height) - 1
        leftMax, rightMax = height[leftIndex],height[rightIndex]

        total = 0

        while leftIndex<rightIndex:
            if leftMax<rightMax:
                leftIndex+=1
                currentHeight = height[leftIndex]
                leftMax = max(leftMax,currentHeight)
                total += leftMax- currentHeight
            else:
                rightIndex-=1
                currentHeight = height[rightIndex]
                rightMax = max(rightMax, currentHeight)
                total += rightMax - currentHeight

        return total

Solution().trap([4,2,0,3,2,5])