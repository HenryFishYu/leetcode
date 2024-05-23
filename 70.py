class Solution:
    def climbStairs(self, n: int) -> int:
        if n<3:
            return n
        first = 1
        second = 2
        current = None
        for _ in range(n-2):
            current = first+second
            first,second = second,current
        return current

