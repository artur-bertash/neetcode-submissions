class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        seen = set()
        l = 0
        seen.add(s[0])
        longest = 0

        for r in range(1, len(s)):
            
            while  s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            longest = max(len(seen), longest)
            
        return max(longest, len(seen))
