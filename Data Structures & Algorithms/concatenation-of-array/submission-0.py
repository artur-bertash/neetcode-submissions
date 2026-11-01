class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums) * 2
        print
        for a in range(len(ans)):
            b = a % len(nums)
            ans[a] = nums[b]
        return ans