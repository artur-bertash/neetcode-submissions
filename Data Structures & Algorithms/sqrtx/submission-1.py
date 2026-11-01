class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x 
        # we got x and looking for sqrt(x) rounded down
        # let it be r so r^2 <= x <= (r + 1)^2
        # which means we need the largest r such that
        # r^2 <= x
        # which means it has a transition point as it is monotonically increasing
        best = 0

        while l <= r:
            m = (l + r) // 2
            if m * m < x:
                best = m
                l = m  + 1
            elif m * m > x:
                r = m - 1
            else:
                return m
        return best
            