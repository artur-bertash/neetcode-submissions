class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = -1
        coun = 0

        for n in nums:
            if n != maj:
                coun -= 1
                if coun <= 0:
                    coun = 1
                    maj = n
            else:
                coun += 1
        return maj