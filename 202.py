class Solution:
    def isHappy(self, n: int) -> bool:
        map = {}
        while n!=1:
            if n in map:
                return False
            map[n] = True
            temp = 0
            while n>0:
                temp += (n%10)**2
                n = n//10
            n = temp

        return True