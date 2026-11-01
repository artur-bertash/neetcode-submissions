class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        best = len(nums)

        while l <= r:
            m = (l + r) // 2

            if nums[m] >= target:
                best = m
                r = m - 1
            else:
                l = m + 1
        return best