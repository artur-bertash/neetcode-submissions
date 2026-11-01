class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = curr = 0
        shortest = float("+inf")
        for r in range(len(nums)):
            curr += nums[r]
            if curr < target:
                continue
            while curr - nums[l] >= target:
                curr -= nums[l]
                l += 1
            shortest = min(r - l + 1, shortest)
        
        return shortest if shortest != float("+inf") else 0