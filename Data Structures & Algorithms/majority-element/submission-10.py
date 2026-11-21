class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = -1
        coun = 0

        for n in nums:
            if maj != n:
                coun -= 1
            if coun <= 0:
                maj = n
                coun = 1
                continue
            coun += 1
        return maj