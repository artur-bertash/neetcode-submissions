class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        best = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] >= nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m
                best = m
        return nums[best]