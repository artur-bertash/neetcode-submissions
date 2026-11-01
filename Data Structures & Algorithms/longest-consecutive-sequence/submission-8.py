class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        lgst = 0
        curr = 0
        prev = float("-inf")

        for n in nums:
            if n == prev + 1:
                curr+=1
            elif n == prev:
                continue
            else:
                curr = 1
            lgst = max(lgst, curr)
            prev = n
        return lgst