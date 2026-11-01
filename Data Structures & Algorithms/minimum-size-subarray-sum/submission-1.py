class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        shortest = float("+inf")
        for i in range(len(nums)):
            curr = 0
            for j in range(i, len(nums)):
                curr += nums[j]
                if curr >= target:
                    shortest = min(shortest, j - i + 1)
                    break
        return shortest if shortest != float("+inf") else 0