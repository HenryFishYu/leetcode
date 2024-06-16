from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        def count_valid_potions(spell: int)->int:
            l,r = 0,len(potions)
            mid = (l + r) // 2
            while l<=r:
                if spell*potions[mid]<success:
                    l = mid+1
                else:
                    r = mid-1
                mid = (l + r) // 2
            return len(potions)-mid

        for spell in spells:
            res.append(count_valid_potions(spell))
        return res

print(Solution().successfulPairs([3,1,2],[8,5,8],16))




