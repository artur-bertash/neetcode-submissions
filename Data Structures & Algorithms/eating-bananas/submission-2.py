class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # total_time <= h
        # there is a transition point as time goes can't can't can't can can 
        def helper(speed):
            hours = 0
            for p in piles:
                hours += p // speed
                if p % speed:
                    hours += 1
                if hours > h:
                    return False
            return True

        l, r = 1, max(piles)
        best = max(piles)

        while l <= r:
            m = (l + r) // 2

            if not helper(m):
                
                l = m + 1
            else:
                best = m
                r = m - 1
        return best