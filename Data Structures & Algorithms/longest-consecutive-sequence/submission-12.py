class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        allEl = set(nums)
        c = 0

        for n in allEl:
            cur = 0 
            while n in allEl:
                n += 1
                cur  += 1
            c = max(c, cur )
        return c 