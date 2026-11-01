class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        best = 0

        while l <= r:
            m = (l + r) // 2
            if nums[m] < target: # everyting < l is less than target
                l = m + 1
                best = m + 1
            elif nums[m] > target: # everything > r is more than target
                
                r = m - 1
            else:
                return m
        return best 