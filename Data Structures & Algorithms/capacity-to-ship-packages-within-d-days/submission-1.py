class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # there is a transition in capacities whether they can ship within days days ( <= days)
        # e.g. 1 can't 2 can't2 3 can't 4 can 5 cant etc
        # returns how many days for wCheck
        def helper(wCheck):
            curWeight = 0
            dCurr = 0
            for w in weights:
                if curWeight + w > wCheck:
                    dCurr += 1
                    curWeight = w
                else:
                    curWeight += w
            return dCurr if not curWeight else dCurr + 1
        
        l, r = max(weights), sum(weights)
        best = sum(weights)

        while l <= r:
            m = (l + r) // 2
            if helper(m) <= days:
                best = m
                r = m - 1
            elif helper(m) > days:
                l = m + 1

        return best

