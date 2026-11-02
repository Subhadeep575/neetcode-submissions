class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        count = 0
        current = 0
        maxLength = 0
        for num in nums:
            if(num-1 not in nums):
                current = num
                count = 1
            while(current+1 in nums):
                count += 1
                current += 1
            maxLength = max(count,maxLength)
        return maxLength