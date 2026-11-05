class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
       
        nums.sort()
        res = []

        for i1 in range(len(nums) - 3):
            if i1 > 0 and nums[i1 - 1] == nums[i1]:
                continue

            for i2 in range(i1 + 1, len(nums) - 2):
                if i2 > 0 and nums[i2 - 1] == nums[i2]:
                    continue
                seen = set()
                for i3 in range(i2 + 1, len(nums)):
                    sm = nums[i1] + nums[i2] + nums[i3]
                    diff = target - sm
                    if diff in seen:
                        temp = [nums[i1], nums[i2], diff, nums[i3]]
                        if not res or res[-1] != temp:
                            res.append(temp)
                    seen.add(nums[i3])
        return res