class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = 0
        for i in range(len(nums)):
            sm = 0
            for j in range(i, len(nums)):
                sm += nums[j]
                if sm == k:
                    counter+=1
                
        return counter