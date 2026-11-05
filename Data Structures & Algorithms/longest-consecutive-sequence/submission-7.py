class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        nums.sort()
        longest = 0
        curr_len = 0
        prev = float("inf")

        for n in nums:
            if n != prev + 1:
                curr_len = 1
            longest = max(curr_len, longest)
            curr_len +=1
            prev = n
            

        return longest + 1

        