class Solution:
    def reverseBits(self, n: int) -> int:
        return int(f'{n:032b}'[::-1], 2)

print(Solution().reverseBits(43261596))