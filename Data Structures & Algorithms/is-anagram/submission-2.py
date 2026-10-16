class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if(len(s) != len(t)):
            return False
        freqOfs = {}
        freqOft = {}

        for ch in s:
            freqOfs[ch] = freqOfs.get(ch,0)+1
        for ch in t:
            freqOft[ch] = freqOft.get(ch,0)+1
        return freqOfs == freqOft