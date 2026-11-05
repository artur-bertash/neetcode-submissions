class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        for  a in range(n):
            if nums[a] > 0:
                break
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            for b in range(a + 1, n):
                if b > a + 1 and nums[b - 1] == nums[b]:
                    continue
                l, r = b + 1, len(nums) - 1

                while l < r:
                    sm = nums[a] + nums[b] + nums[l] + nums[r]
                    if sm < target:
                        l += 1
                    elif sm > target:
                        r -= 1
                    else:
                        res.append([nums[a], nums[b], nums[l], nums[r]])
                        r -= 1
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
        return res
