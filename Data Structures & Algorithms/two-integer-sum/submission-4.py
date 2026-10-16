class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        storeIdx = {}
        for i,num in enumerate(nums):
            need = target - num
            if(need in storeIdx):
                return [storeIdx[need],i]
            storeIdx[num] = i    