class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m = len(strs[0])
        res = ""

        for ch in range(len(strs[0])):
            for i in range(1, len(strs)):
                if not strs[i]:
                    return ""
                if strs[i][ch] != strs[0][ch]:
                    return res
            res+=strs[0][ch]
        return res