class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s_array = sentence.split(" ")

        for i in range(len(s_array)):
            if s_array[i][0]!=s_array[i-1][-1]:
                return False
        return True