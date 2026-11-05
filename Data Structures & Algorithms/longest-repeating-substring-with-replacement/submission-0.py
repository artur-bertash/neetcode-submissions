class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                count = [0] * 26
                
                for p in range(i, j + 1):
                    count[ord(s[p]) - ord('A')]+= 1
                
                most_common = max(count)
                length = j - i + 1
                changed_needed = length - most_common
                if changed_needed <= k:
                    best = max(best, length)
        return best