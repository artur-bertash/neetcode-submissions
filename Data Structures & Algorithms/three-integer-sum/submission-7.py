class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            mp = set()
            for j in range(i + 1, len(nums)):

                needed = -(nums[i] + nums[j])
                if needed in mp:
                    temp = [nums[i], nums[j], needed]
                    if not res or res[-1] != temp:
                        res.append(temp)
                mp.add(nums[j])
        return res

