class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mP = float("inf")
        c = 0
        for n in nums:
            if c == 0 and n != mP:
                mP = n
                c += 1
                continue
            c += 1
        return mP