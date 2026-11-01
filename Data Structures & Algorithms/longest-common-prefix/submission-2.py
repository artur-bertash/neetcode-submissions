class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        w = ""
        m = float("+inf")
        res = ""

        for word in strs:
            if len(word) < m:
                m = int(len(word))
                w = word
        
        for ch in range(m):
            for i in range(1, len(strs)):
                if strs[i][ch] != strs[i - 1][ch]:
                    return res
            res+=w[ch]
        return res
