class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = 0
        people.sort()
        l, r = 0, len(people) - 1
        while l <= r:
            if people[r] + people[l] <= limit:
                count +=1
                r-=1
                l +=1
            elif people[r] <= limit:
                count+=1
                r-=1
        return count
# 1 1 1 2 3 4
        