class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = {}

        for n in nums:
            mp[n] = mp.get(n, 0) + 1
        
        cm = 0
        val = 0
        for key, count in mp.items():
            if cm < count:
                val = key
                cm = count
        return val