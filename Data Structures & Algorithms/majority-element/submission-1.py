class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = {}
        cm = 0
        val = 0

        for n in nums:
            mp[n] = mp.get(n, 0) + 1
            if mp[n] > cm:
                cm = mp[n]
                val = n
        
        
        return val