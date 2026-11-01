class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1 2 4 6 
        # 1 1  2  8  48 
        # 48 48 24 6 1
        # for pref[i] it's running sum of nums[i -3] + nums[i - 2] + nums[i - 1]
        # posft[i] = nums[i + 1] + nums[i + 2 ] etc
        n = len(nums)
        postf = [1] * (n + 1) 
        pref = [1] * (n + 1)
        s = 1
        f = 1

        for i in range(n):
            pref[i + 1] = pref[i] * nums[i]
            postf[(n + 1) - i - 2] = nums[n - i - 1] * postf[(n + 1) - i - 1]
        
        res = [1] * n

        for i in range(n):
            res[i] = pref[i] * postf[i + 1]
        return res
        

        
