class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        prev = float("-inf")
        nums.sort()
        for i in range(len(nums) - 2):
            

            seen = set()

            for j in range(i + 1, len(nums)):
                diff = nums[j] + nums[i]
                if -diff in seen:
                    temp = [nums[i], nums[j], -diff]
                    if not res or res[-1] != temp:
                        res.append(temp)
                seen.add(nums[j])
        return res

# -1 0 1 2 -1 -4
# -4 -1 -1 0 1  1 2 2
