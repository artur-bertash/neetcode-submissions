class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # keep track of two most popular elements
        a = b = float('inf')
        aC, bC = 0, 0 
        
        for n in nums:
            # think of array as 
            # len(arr) >= 3 * floor(n / 3)

            if not aC and b!=n:
                a = n
                aC = 1
                continue
            if not bC and a !=n:
                b = n
                bC = 1
                continue

            if n == a:
                aC += 1
            elif n == b:
                bC += 1
            else:
                aC -= 1
                bC -= 1
        res = []
        
        return [x for x in (a, b) if nums.count(x) > len(nums) // 3]