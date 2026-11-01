class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        lgst = curr = 1
        nums = sorted(set(nums))

        for i in range(1, len(nums)):
            if nums[i - 1] + 1 == nums[i]:
                curr += 1
            else: 
                curr = 1
            lgst = max(lgst, curr)
        return lgst