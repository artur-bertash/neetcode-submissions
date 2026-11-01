class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        cm = 0
        val = 0

        for n in nums:
            mp[n] += 1
            if mp[n] > len(nums) // 2:
                cm = mp[n]
                val = n
        
        
        return val