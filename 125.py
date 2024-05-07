import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed = re.findall(r'[a-z]',s.lower())
        return processed==processed[::-1]

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))