class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixMap = defaultdict(int)
        res = 0
        curPrefix = 0
        prefixMap[0] = 1

        for n in nums:
            curPrefix += n
            # we want curPrefix - oldPrefix = k
            diff = curPrefix - k
            res += prefixMap[diff]
            prefixMap[curPrefix] += 1
        return res     