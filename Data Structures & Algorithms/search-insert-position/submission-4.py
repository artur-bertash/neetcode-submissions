class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        best = len(nums)

        while l <= r:
            m = (l + r) // 2
            if nums[m] < target: # everyting < l is less than target
                l = m + 1
                best = m
            elif nums[m] > target: # everything > r is more than target
                
                r = m - 1
            else:
                return m
        return best + 1