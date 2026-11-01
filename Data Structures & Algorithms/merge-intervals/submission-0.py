class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        prev = None

        for cur in intervals:
            if not prev:
                prev = cur
                continue

            # [-10, 2] [-5, 1] [-3, 100]
            if prev[1] >= cur[0]:
                prev[1] = max(prev[1], cur[1])
            else:
                res.append(prev)
                prev = cur
        if prev:
            res.append(prev)
        return res
