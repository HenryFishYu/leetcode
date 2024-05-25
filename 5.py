class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        max_len = 0
        for i in range(len(s)):
            temp_len = 0
            while i-temp_len>=0 and i+temp_len<len(s) and s[i-temp_len] == s[i+temp_len]:
                if 2*temp_len+1>max_len:
                    max_len = 2*temp_len+1
                    res = s[i-temp_len:i+temp_len+1]
                temp_len += 1

            temp_len = 0
            while i - temp_len >= 0 and i+1 + temp_len < len(s) and s[i - temp_len] == s[i + temp_len+1]:
                if 2 * (temp_len + 1) > max_len:
                    max_len = 2 * (temp_len + 1)
                    res = s[i - temp_len:i + temp_len + 2]
                temp_len += 1

        return res