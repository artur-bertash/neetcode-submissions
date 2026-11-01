class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = k % len(nums)
        nums[:] = nums[::-1]
        nums[:i] = nums[:i][::-1]
        nums[i:] = nums[i:][::-1]
        


        
        
