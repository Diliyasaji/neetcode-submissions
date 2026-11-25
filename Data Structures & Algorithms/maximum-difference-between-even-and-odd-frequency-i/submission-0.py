class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}
        for char in s:
            if char in freq:
                freq[char]+=1
            else:
                freq[char]=1
        oddFreq = []
        evenFreq = []

        for count in freq.values():
            if count%2 !=0:
                oddFreq.append(count)
            else:
                evenFreq.append(count)
        return max(oddFreq) - max(evenFreq)
        