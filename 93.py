from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        res = []

        def dfs(leftIndex: int, temp: list[str]):
            if leftIndex == n and len(temp) == 4:
                res.append(".".join(temp))
                return

            if len(temp) > 4 or (n - leftIndex) > 3 * (4 - len(temp)):
                return

            for length in range(1, 4):
                if leftIndex + length > n:  # 剩余字符不足
                    break
                segment = s[leftIndex:leftIndex + length]

                # 检查是否合法：不能有前导零，且值在 0-255 之间
                if (segment[0] == '0' and len(segment) > 1) or int(segment) > 255:
                    continue

                temp.append(segment)
                dfs(leftIndex + length, temp)
                temp.pop()  # 回溯


        dfs(0,[])
        return res

print(Solution().restoreIpAddresses("101023"))
