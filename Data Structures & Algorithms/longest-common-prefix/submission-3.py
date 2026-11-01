class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]

        for i in range(1, len(strs)):
            j = 0

            while j < min(len(pref), len(strs[i])):
                if pref[j] != strs[i][j]:
                    break 
                j+=1
            pref = pref[:j]
        return pref