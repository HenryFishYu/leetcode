from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftIndex= 0
        rightIndex = len(numbers)-1

        while leftIndex<rightIndex:
            res = numbers[leftIndex]+numbers[rightIndex]
            if res==target:
                return [leftIndex+1,rightIndex+1]
            if res>target:
                rightIndex-=1
                continue
            if res<target:
                leftIndex+=1
                continue

        return []