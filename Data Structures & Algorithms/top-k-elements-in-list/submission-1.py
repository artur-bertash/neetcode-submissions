class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for _ in range(len(nums) + 1)]
        mp = defaultdict(int)

        for n in nums:
            mp[n] += 1
        
        for n, c in mp.items():
            count[c].append(n)
        res = []

        for i in range(len(count) - 1, 0, -1):
            if not k:
                return res
            for n in count[i]:
                res.append(n)
                k-=1
        return res
        
        
