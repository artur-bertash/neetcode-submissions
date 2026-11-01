class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = curr = 0
        shortest = float("+inf")
        for r in range(len(nums)):
            curr += nums[r]

            while curr >= target:
                shortest = min(shortest, r - l + 1)
                curr -= nums[l]
                l += 1

        return shortest if shortest != float("+inf") else 0