class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # 
        # not A and B
        best1 = best2 = -1
        count1 = count2 = 0
        for n in nums:
            if n == best1 or n == best2:
                count1 += 1 if n == best1 else 0
                count2 += 1 if n == best2 else 0
            else:
                
                
                if count1 <= 0:
                    best1 = n 
                    count1 = 1
                    continue
                if count2 <= 0:
                    best2 = n
                    count2 = 1
                    continue
                count1 -= 1 
                count2 -= 1 
        return [x for x in [best1, best2] if nums.count(x) > len(nums) // 3]
