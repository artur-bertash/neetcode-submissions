class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        for r in range(len(nums)):
            if nums[r] in window:
                return True
            
            if len(window) >= k :
                window.remove(nums[r - k]) 

            window.add(nums[r])
        return False
            