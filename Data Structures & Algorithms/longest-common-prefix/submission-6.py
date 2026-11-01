class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]

        for word in strs:
            i = 0
            while i < len(res) and i < len(word) and res[i] == word[i]:
                i += 1
            res = res[:i]
            if not res:
                break
        return res