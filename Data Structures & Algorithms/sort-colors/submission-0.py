class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = w = b = 0

        for n in nums:
            r += 1 if n == 0 else 0
            w += 1 if n == 1 else 0
            b += 1 if n == 2 else 0
        
        i = 0
        while r:
            nums[i] = 0
            r -= 1
            i += 1
        
        while w:
            nums[i] = 1
            w -= 1
            i += 1
        
        while b:
            nums[i] = 2
            b -= 1
            i += 1
