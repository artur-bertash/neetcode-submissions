class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        can = 0
        ct = 0

        for n in nums: 
            if ct == 0: 
                can = n
            ct += (1 if n == can else - 1)
        return can