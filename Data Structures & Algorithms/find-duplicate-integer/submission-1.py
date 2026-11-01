class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        n = len(nums)
        slow = fast = 0

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]

            if slow == fast:
                break
        # slow walked x + y
        # fast walked 2(x + y)
        # but now both fast and slow point at y past meeting point
        # so by adding it resets since x + y is some multple of the length
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

