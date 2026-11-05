class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        prev = float("-inf")
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            seen = set()

            for j in range(i + 1, len(nums)):
                diff = nums[j] + nums[i]
                if -diff in seen:
                    res.append([nums[i], nums[j], -diff])
                seen.add(nums[j])
        return res

# -1 0 1 2 -1 -4
# -4 -1 -1 0 1  1 2 2
