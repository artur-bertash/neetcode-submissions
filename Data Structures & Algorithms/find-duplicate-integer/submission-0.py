class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        n = len(nums)
        slow = fast = 0

        while fast < n :
            fast = nums[nums[fast]]
            slow = nums[slow]

            if slow == fast:
                return slow
        return -1

