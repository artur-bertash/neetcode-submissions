class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        seen = {}
        longest = 0

        for n in nums: 
            if (n - 1) in seen:
                seen[n] = seen[n - 1] + 1
            seen[n] = 1
        return longest

        