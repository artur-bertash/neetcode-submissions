class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        prev = float("-inf")
        for n in nums:
            if n == prev:
                continue
            nums[i] = n
            i+=1
            prev = n
        return i
