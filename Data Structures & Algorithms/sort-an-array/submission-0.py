class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        lst = nums
        if len(lst) <= 1:
            return lst
        i = len(lst) // 2
        left = self.sortArray(lst[:i])
        right = self.sortArray(lst[i:])

        i = j = 0
        res = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i+=1
            else:
                res.append(right[j]) 
                j+=1
        res.extend(left[i:])
        res.extend(right[j:])
        return res