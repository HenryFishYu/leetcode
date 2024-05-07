from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line,length = [],0
        for word in words:
            if len(line)+length+len(word)<=maxWidth:
                line.append(word)
                length+=len(word)
                continue

            gaps = max(1,len(line)-1)

            basicSpace = (maxWidth-length) // gaps
            extraSpace = (maxWidth-length) % gaps

            for i in range(max(1,len(line)-1)):
                line[i] += " "*basicSpace
                if extraSpace:
                    line[i] += " "
                    extraSpace -= 1

            res.append("".join(line))
            line, length = [word], len(word)

        tmpRes = " ".join(line)
        tmpRes += " "*(maxWidth-len(tmpRes))
        res.append(tmpRes)
        return res




Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."],16)
