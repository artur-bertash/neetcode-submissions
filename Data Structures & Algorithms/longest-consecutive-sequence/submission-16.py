class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        allEl = set(nums)

        for n in allEl:
            if n - 1 not in allEl:
                cur = 0
                while n in allEl:
                    n += 1
                    cur += 1
                res = max(cur, res)
        return res



