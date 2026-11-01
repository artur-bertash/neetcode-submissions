class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i1 in range(len(nums)):
            if i1 > 0 and nums[i1] == nums[i1 - 1]:
                continue
            l, r = i1 + 1, len(nums) - 1

            while l < r:
                sm = nums[l] + nums[r] + nums[i1]
                if sm < 0:
                    l+= 1
                    continue
                elif sm > 0:
                    r -= 1
                    continue
                else:
                    res.append([nums[l], nums[r], nums[i1]])
                    l+=1 
                    r-=1
                    while l < r and nums[l] == nums[l - 1]:
                        l+=1
        return res
                        # -2 -2 0 0 2 2 
# -1 -1 0 1 1 