class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        seen = set(nums[:k])

        for r in range(k, len(nums)):
            if nums[r] in seen:
                return True
            
            seen.add(nums[r])
            seen.remove(nums[l])
            l += 1
        return False
            
