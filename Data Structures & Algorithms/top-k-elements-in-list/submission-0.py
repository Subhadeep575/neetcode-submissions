class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        result = []
        for num in nums:
            freq[num] = freq.get(num,0) + 1

        while(k>0):
            maxCount = 0
            maxNum = None
            for num, count in freq.items():
                if(count > maxCount):
                    maxCount = count
                    maxNum = num
            result.append(maxNum)
            freq.pop(maxNum)
            k -= 1
        return result