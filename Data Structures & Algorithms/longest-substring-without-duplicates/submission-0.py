class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        right = 0
        maxLength = 0
        for ch in s :
            while(ch in seen):
                seen.remove(s[left])
                left += 1
            seen.add(ch)
            right += 1
            maxLength = max(maxLength, right - left)
        return maxLength