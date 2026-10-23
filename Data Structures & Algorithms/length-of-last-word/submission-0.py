class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for char in reversed(s):
            if char == ' ':
                if count>0:
                    break
            else:
                count+= 1
        return count
       

        