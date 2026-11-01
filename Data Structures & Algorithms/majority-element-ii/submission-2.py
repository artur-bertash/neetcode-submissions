class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1 = g1 = g2 = c2 = 0
        for n in nums: 
            if g1 == n: c1 += 1; continue
            if g2 == n: c2 += 1; continue

            if not c1: g1 = n; c1 = 1; continue
            if not c2: g2 = n; c2 = 1; continue

            c1 -= 1
            c2 -= 1
        return [x for x in [g1, g2] if nums.count(x) > len(nums) // 3]