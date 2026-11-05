class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_seen = {0: 1}
        res = sm = 0

        for n in nums:
            sm += n 
            # k = prefix[i] - prefix[j] where k = sum(prefix[j + 1:i])
            left_prefix = sm - k
            prefix_seen[sm] = prefix_seen.get(sm, 0) + 1
            res+= prefix_seen.get(left_prefix, 0)
        return res