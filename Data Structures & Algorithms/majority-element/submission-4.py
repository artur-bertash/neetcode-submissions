class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        bit = [0] * 32

        for n in nums: 
            for i in range(32):
                bit[i] += ((n >> i)  & 1)
        res = 0
        for i in range(32):
            if bit[i] > (len(nums) // 2):
                if i == 31:
                    res -= (1 << i)
                else:
                    res |= (1 << i)
        return res
