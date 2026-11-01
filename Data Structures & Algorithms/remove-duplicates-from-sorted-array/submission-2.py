class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = float("inf")
        i = 0

        for n in nums:
            if n != prev:
                nums[i] = n
                i += 1
            prev = n
        
        return i