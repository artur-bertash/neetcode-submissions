class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        h = []


        for r in range(len(arr)):
            heapq.heappush(h, (-abs(arr[r] - x), -arr[r]))
            if len(h) > k:
                heapq.heappop(h)
        return sorted(-val for _, val in h)