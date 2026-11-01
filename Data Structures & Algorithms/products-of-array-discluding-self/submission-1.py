class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCounter = 0
        product = 1

        for n in nums:
            if n == 0:
                zeroCounter += 1
            else:
                product *= n
        
        for i in range(len(nums)):
            if zeroCounter == 0:
                nums[i] = product // nums[i]
            elif zeroCounter == 1:
                if nums[i] == 0:
                    nums[i] = product
                else:
                    nums[i] = 0
            else:
                nums[i] = 0
        return nums
