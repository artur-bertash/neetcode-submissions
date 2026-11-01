class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        best = float("inf")
        window = 0
        l = 0

        for r in range(len(nums)):
            window += nums[r]
            while window >= target:
                best = min(r - l + 1, best)
                window -= nums[l]
                l += 1

        return best if best != float("inf") else 0 
            
            
            

            