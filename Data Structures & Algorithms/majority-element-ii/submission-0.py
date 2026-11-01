class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        g1 = c1 = 0
        g2 = c2 = 0

        for n in nums: 
            if n == g1:
                c1 += 3
                continue
            if n == g2:
                c2 += 3
                continue

            if not c1:
                g1 = n
                c1 = 3
                continue
            if not c2:
                g2 = n
                c2 = 3
                continue
            
            if n == g1:
                c1 += 3
                continue
            if n == g2:
                c2 += 3
                continue

            c1 -= 3
            c2 -= 3
        return [x for x in (g1, g2) if nums.count(x) > len(nums) // 3]
            