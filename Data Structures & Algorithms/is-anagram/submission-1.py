class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for i in t:
            if i in freq:
                freq[i] = freq[i]+1
            else:
                freq[i] = 1
        freq1={}
        for i in s:
            if i in freq1:
                freq1[i] = freq1[i]+1
            else:
                freq1[i] = 1
        
        if freq == freq1:
            return True
        return False