class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        resArr = [[] for _ in range(numRows)]
        totalLen = numRows*2-2

        for i in range(len(s)):
            left = i%totalLen
            if left>=numRows:
                left = totalLen-left
            resArr[left].append(s[i])

        res = ""
        for arr in resArr:
            res+= "".join(arr)
        return res

print(Solution().convert("PAYPALISHIRING",3))



