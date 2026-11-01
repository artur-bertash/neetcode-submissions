class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i1 in range(len(nums) - 3):
            if i1 > 0 and nums[i1 -1] == nums[i1]:
                continue
            
            for i2 in range(i1 + 1, len(nums) - 2):
                if i2 > i1 + 1 and nums[i2 - 1] == nums[i2]:
                    continue
                
                l, r = i2 + 1, len(nums) - 1

                while l < r:
                    sm = nums[i1] + nums[i2] + nums[l] + nums[r]

                    if sm < target:
                        l+=1 
                    elif sm > target:
                        r-= 1
                    else:
                        res.append([nums[i1], nums[i2], nums[l], nums[r]])
                        l+=1
                        r-=1
                        while l < r and nums[l] == nums[l - 1]:
                            l+=1
        return res