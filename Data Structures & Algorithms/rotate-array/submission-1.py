class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a,b = k % len(nums), 0

        while a < len(nums):
            nums[a], nums[b] = nums[b], nums[a]
            a+=1 
            b+=1
