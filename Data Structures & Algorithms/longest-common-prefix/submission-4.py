class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for ch in range(len(strs[0])):
            for w in strs:
                if ch >= min(len(w), len(strs[0])) or w[ch] != strs[0][ch]:
                    return w[:ch]
        return strs[0]