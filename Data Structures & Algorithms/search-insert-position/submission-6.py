class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # let m = [false, false, false, true, true, true ..]
        # where the transition point is where n >= target
        l, r = 0, len(nums) - 1
        best = len(nums) 

        while l <= r:
            m = (l + r) // 2

            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                best = m
                r = m - 1
            else:
                return m
        return best