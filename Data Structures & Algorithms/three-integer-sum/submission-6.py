class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            mp = defaultdict(int)
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                needed = -(nums[i] + nums[j])
                if needed in mp:
                    res.append([nums[i], nums[j], needed])
                mp[nums[j]] = j
        return res

