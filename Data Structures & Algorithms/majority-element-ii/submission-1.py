class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        for n in nums: 
            count[n] += 1

            if len(count) <= 2:
                continue
            
            new_count = defaultdict(int)
            for a, c in count.items():
                if c > 1:
                    new_count[a] = count[a] - 1
        return [x for x in count if nums.count(x) > len(nums) // 3]

