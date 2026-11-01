class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        lgst = 0

        for n in numSet: 
            if (n - 1) not in numSet:
                curr = 0
                while n in numSet:
                    curr+=1
                    n+=1
                lgst = max(curr, lgst)
        return lgst