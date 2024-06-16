class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        and_ab = a & b
        or_ab = a | b
        res = 0

        while and_ab>0 or or_ab>0 or c>0:
            last_and_ab = and_ab & 1
            last_or_ab = or_ab & 1
            last_c = c & 1

            and_ab = and_ab>>1
            or_ab = or_ab>>1
            c = c>>1

            if last_or_ab==last_c:
                continue

            if last_or_ab==0:
                res += 1
                continue

            if last_or_ab==1:
                if last_and_ab==1:
                    res+=2
                    continue
                if last_and_ab==0:
                    res+=1
                    continue

        return res

print(Solution().minFlips(2,6,5))


