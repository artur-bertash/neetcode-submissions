class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r: 
            if nums[r] == val:
                r-=1
                continue
            if nums[l] != val:
                l+=1
                continue
            
            nums[r], nums[l] = nums[l], nums[r]
            r-=1
            l+=1
        return l + 1